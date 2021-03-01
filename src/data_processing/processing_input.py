import pandas as pd
import pickle5 as pickle

# file = open("model/One_Hot_Encoder.pkl", "rb")

one_hot = pickle.load(open("model/One_Hot_Encoder.pkl", "rb"))


def process_input(input_data):
    """
    Function which One Hot Encodes input from API.
    :param input_data: sent to API by the user
    :return: input data, encoded features
    """
    try:
        dataframe = pd.DataFrame.from_dict(input_data, orient="index").T
        dataframe[["year", "rating", "metascore", "total_votes"]] = dataframe[
            ["year", "rating", "metascore", "total_votes"]
        ].astype(float)
        encoded_features = one_hot.transform(dataframe)

        return input_data, encoded_features
    except:
        print("here is a problem with processing input function")
