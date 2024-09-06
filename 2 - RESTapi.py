# Python 3.8.10

import requests

NAME = 0
IMDB_RATING = 1

# PREGUNTAS: ¿Qué devolver en caso de que ninguna serie sea parte del género buscado?
#            ¿Dejo el main con que el probé la función?
#            ¿Es case insensitive la entrada del usuario sobre el género?

url = "https://jsonmock.hackerrank.com/api/tvseries"

def bestInGenre(genre):
    heighest_rated_serie = (f"Ninguna serie forma parte del género {genre}", -1) # Knowing all ratings are equal or greater than 0
    tvSeries = requests.get(url).json()

    totalPages = tvSeries["total_pages"]

    for pageNumber in range(1, totalPages + 1):
        if pageNumber != 1:
            tvSeries = requests.get(url + f"?page={pageNumber}").json()

        for tvSerie in tvSeries["data"]:
            if genre in tvSerie["genre"].split(", "):
                if tvSerie["imdb_rating"] > heighest_rated_serie[IMDB_RATING] or \
                    (tvSerie["imdb_rating"] == heighest_rated_serie[IMDB_RATING] and tvSerie["name"] < heighest_rated_serie[NAME]):
                    heighest_rated_serie = (tvSerie["name"], tvSerie["imdb_rating"])

    return heighest_rated_serie[NAME]



print(bestInGenre('Action'))