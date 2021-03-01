import requests
import json

resp = requests.post(
    "https://imdb-prediction-api.herokuapp.com/predict",
    data=json.dumps(
        {
            "features": [
                {
                    "year": 1990.0,
                    "certificate": "R",
                    "length": 100.0,
                    "category": "Adventure",
                    "rating": 5.6,
                    "metascore": 60.0,
                    "total_votes": 251445.0,
                    "first_genre": "Animation",
                    "second_genre": "Action",
                    "third_genre": "Adventure",
                }
            ]
        }
    ),
)
print(json.loads(resp.text))


resp = requests.get("https://imdb-prediction-api.herokuapp.com/select")
# respa = requests.get('http://127.0.0.1:5000/select')
print(json.loads(resp.text))
# print(json.loads(respa.text))
#
# assert resp.text == respa.text
