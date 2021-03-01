## IMDB Movie US Gross Profit Prediction API  

### Turing College Capstone Project part 2  

You can find Capstone Project part 1 [here](https://github.com/mantaspieza/IMDB_Movie_Scraper.git)  

#### General Info
In this repository you will find IMDB movie profit prediction API created using flask and deployed on Heroku platform.  

After the required information is scraped from IMDB (for more details click [here](https://github.com/mantaspieza/IMDB_Movie_Scraper.git)) .csv file is cleaned and prepared for One Hot Encoding.  
Encoded information is train test splited and Linear Regression model is fit on training set to predicts US box office price of the movie. (r2 score on test set is 0.91)  

Upon each request sent to the API the predicted earnings is provided.  
Request information and predicted earnings are stored at postgreSQL database on Heroku platform.  

#### API info
You can reach the deployed model:  
[https://imdb-prediction-api.herokuapp.com/](https://imdb-prediction-api.herokuapp.com/)  

To retrieve ten last predictions you can use `/select` endpoint:  
[https://imdb-prediction-api.herokuapp.com/select](https://imdb-prediction-api.herokuapp.com/select)  

Also you can use postman  
or [requests](https://requests.readthedocs.io/en/master/) and [json](https://docs.python.org/3/library/json.html) libraries:  
```
import requests
import json

ten_last_database_inputs = requests.get("https://imdb-prediction-api.herokuapp.com/select")
print(json.loads(ten_last_database_inputs.text)
```  

`Predict` method accepts json type inputs with features and returns predicted movie earnings.  
It is possible to send POST requests via postman:
https://imdb-prediction-api.herokuapp.com/predict
```
{"features":
    [{"year": 2000.0, "certificate": "V", "length": 80.0, "category": "Sci-Fi", "rating": 3.6, "metascore": 60.0,
     "total_votes": 251445.0, "first_genre": "Animation", "second_genre": "Action", "third_genre": "Adventure"}]}
     
{"features":
    [{"year": 1990.0, "certificate": "R", "length": 100.0, "category": "Adventure", "rating": 5.6, "metascore": 60.0,
     "total_votes": 251445.0, "first_genre": "Animation", "second_genre": "Action", "third_genre": "Adventure"}]}
```

#### For future requests    
As data was encoded using OneHotEncoder, data is treated as categorical instead of continuous therefore posible input features are limited to the scope of the training dataset.

Possible prediction inputs:  
* year (float)
* certificate (string): R, PG-13, PG, V, G, ,N-13, N-16, N-7, N-18, NC-17, "Not Rated"
* Length fo the movie (float)
* Category (string): Drama, Comedy, Thriller, Romance, Action, Crime, Adventure, Fantasy, Mystery, Sci-Fi, Horror, Animation
* IMDB Rating (float)
* Metascore (float)
* Total votes (float)
* First genre (string): Action, Comedy, Drama, Crime, Animation, Adventure, Biography, Horror, Documentary, Fantasy, Mystery, Romance, Thriller, Musical, Family, Sci-Fi
* Second genre (string): Drama, Adventure, Crime, Comedy, Romance, Mystery, Horror, Fantasy, Thriller, Action, Family, Sci-Fi, Biography, Music, History
* Third genre (string): Thriller, Drama, Romance, Comedy, Fantasy, Sci-Fi, Mystery, Crime, Family, Horror, Adventure, History, Music, Sport, War.

