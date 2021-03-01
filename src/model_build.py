from src.data_processing.data_wrangling import prepare_to_train_test_split
import pickle5 as pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
import pandas as pd


imdb_dataframe = pd.read_csv("../data/processed/processed_imdb_dataframe.csv")

features, target = prepare_to_train_test_split(imdb_dataframe)
encoder = OneHotEncoder(drop="first")
LinReg = LinearRegression()

ohe_features = encoder.fit_transform(features)

x_train, x_test, y_train, y_test = train_test_split(
    ohe_features, target, test_size=0.1, random_state=42
)
LinReg.fit(x_train, y_train)
# r2score = 0.91


with open("model/One_Hot_Encoder.pkl", "wb") as handle:
    pickle.dump(encoder, handle)

with open("model/LinearRegression.pkl", "wb") as handle:
    pickle.dump(LinReg, handle)
