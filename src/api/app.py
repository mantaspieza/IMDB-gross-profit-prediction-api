from src.data_processing.processing_input import process_input
from src import database
import pickle5 as pickle
import json
import psycopg2
from flask import Flask, request
from decouple import config


app = Flask(__name__)

database_url = config("DATABASE_URL")
database_connection = psycopg2.connect(database_url)

model = pickle.load(open("model/LinearRegression.pkl", "rb"))


@app.route("/")
def hello_message():
    return "<h1> Hi and thanks for using this api, to continue please send your request adding route /predict </h1>"


@app.route("/predict", methods=["POST"])
def predict_movie_earnings() -> json:
    """
    Function which receives input from API, process it and writes it to database on Heroku platform.
    :return:
    """
    try:
        requested_data, input_parameters = process_input(
            json.loads(request.data)["features"][0]
        )
    except:
        return json.dumps({"error:": "there is problems with input parameters"}), 400
    try:
        prediction = model.predict(input_parameters)
        predicted_earnings = "%0.2f" % prediction
    except:
        return (
            json.dumps(
                {"error:": "input meanings does not match the training dataset."}
            ),
            400,
        )
    try:

        cursor = database_connection.cursor()
        database.insert_into_table(
            cursor=cursor,
            database_connection=database_connection,
            requested_data=requested_data,
            predicted_earnings=predicted_earnings,
        )
    except:
        return json.dumps({"error:": "unable to upload into Heroku database"}), 500

    return json.dumps({"predicted_earnings": predicted_earnings}), 200


@app.route("/select", methods=["GET"])
def ten_last_requests() -> json:
    """
    Returns 10 latest inputs from postgreSQL database on Heroku platform.
    :return: results
    """
    try:
        cursor = database_connection.cursor()
        results = database.select_recent_requests(cursor=cursor)
        return json.dumps({"ten last requests and predictions": results}), 200
    except:
        return json.dumps({"error": "something went wrong"}), 500


if __name__ == "__main__":
    app.run(debug=True)
