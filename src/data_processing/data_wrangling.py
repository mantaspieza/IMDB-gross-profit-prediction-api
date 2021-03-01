import pandas as pd


def clean_dataframe(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Function which removes Title column and fixes values in "length" column.
    :param dataframe: dataframe received after using IMDB scrapper.
    :return: pandas DataFrame.
    """
    data_copy = dataframe.dropna().copy()
    data_copy["length"] = data_copy["length"].str.replace("min", "")
    data_copy["length"] = data_copy["length"].str.strip().astype(float)

    clean_dataframe = data_copy.drop(["title"], axis=1)
    clean_dataframe.to_csv(r"../../data/cleaned/cleaned.csv", index=False, header=True)
    return clean_dataframe


def expand_dataframe(cleaned_dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Expands genres column in dataframe.
    :param cleaned_dataframe:
    :return:
    """
    expanded_genre_column = pd.DataFrame(
        cleaned_dataframe.genres.str.split(",").tolist(),
        columns=["first_genre", "second_genre", "third_genre"],
    ).reset_index()

    expanded_genre_column.third_genre = expanded_genre_column.third_genre.str.strip()
    expanded_genre_column.second_genre = expanded_genre_column.second_genre.str.strip()

    cleaned_dataframe = cleaned_dataframe.drop(["genres"], axis=1).reset_index()

    expanded_dataframe = pd.concat([cleaned_dataframe, expanded_genre_column], axis=1)
    expanded_dataframe.to_csv(
        r"../../data/processed/processed_imdb_dataframe.csv", index=False, header=True
    )
    return expanded_dataframe


def prepare_to_train_test_split(clean_dataframe: pd.DataFrame):
    """
    Function which does feature engineering and splits cleaned dataframe to features and target variables ready
    to be used for One hot Encoding.
    :param clean_dataframe: pandas dataframe
    :return: pandas Dataframes : features, target
    """

    target = clean_dataframe["US_box_office"].reset_index()
    target = target.drop(["index"], axis=1).astype(int)

    features = clean_dataframe.drop(["US_box_office"], axis=1).reset_index()

    return features, target


def main():
    imdb_dataframe = pd.read_csv("raw/scraped_imdb.csv")
    cleaned_dataframe = clean_dataframe(imdb_dataframe)
    expand_dataframe(cleaned_dataframe)


if __name__ == "__main__":
    main()
