def insert_into_table(
    database_connection, cursor, requested_data: dict, predicted_earnings: str
) -> None:
    """
    Inserts information into predictions table on heroku platform.
    :param database_connection: psycopg2 connection to heroku platform.
    :param cursor: database connection cursor.
    :param requested_data: request information from predictions sent by user
    :param predicted_earnings: generated prediction of deployed model.
    :return: None
    """

    command = f"""INSERT INTO imdb_api_database (year, certificate, length, category, rating, metascore,
             total_votes, first_genre, second_genre, third_genre, predicted_earnings)
             VALUES (
             {float(requested_data['year'])},
             '{requested_data['certificate']}',
             {float(requested_data['length'])},
             '{requested_data['category']}',
             {float(requested_data['rating'])},
             {float(requested_data['metascore'])},
             {float(requested_data['total_votes'])},
             '{requested_data['first_genre']}',
             '{requested_data['second_genre']}',
             '{requested_data['third_genre']}',
             '{predicted_earnings}'
             )"""
    cursor.execute(command)
    database_connection.commit()


def select_recent_requests(cursor):
    """
    Returns 10 latest inputs from postgreSQL database on Heroku platform.
    :return: results
    """
    cursor.execute(
        """
        SELECT * FROM imdb_api_database ORDER BY ID DESC LIMIT 10"""
    )
    rows = cursor.fetchall()
    results = [
        {
            "id": row[0],
            "year": row[1],
            "certificate": row[2],
            "length": row[3],
            "category": row[4],
            "rating": row[5],
            "metascore": row[6],
            "total_votes": row[7],
            "first_genre": row[8],
            "second_genre": row[9],
            "third_genre": row[10],
            "predicted_earnings": row[11],
        }
        for row in rows
    ]

    return results
