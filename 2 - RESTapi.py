# Python 3.8.10

import requests

NAME = 0
IMDB_RATING = 1
IMDB_RATING_SERIES_NOT_FOUND = -1

class SeriesNotFoundException(Exception):
    pass

url = "https://jsonmock.hackerrank.com/api/tvseries"

def bestInGenre(genre):
    heighest_rated_serie = ("", IMDB_RATING_SERIES_NOT_FOUND) 
    try:
        tvSeries = requests.get(url).json()
        totalPages = tvSeries["total_pages"]
    except Exception as e:
        return f"Error al buscar las series: {e}"

    for pageNumber in range(1, totalPages + 1):
        try:
            if pageNumber != 1:
                tvSeries = requests.get(url + f"?page={pageNumber}").json()
        except Exception as e:
            return f"Error al buscar las series: {e}"

        for tvSerie in tvSeries["data"]:
            if genre in tvSerie["genre"].split(", "):
                if tvSerie["imdb_rating"] > heighest_rated_serie[IMDB_RATING] or \
                    (tvSerie["imdb_rating"] == heighest_rated_serie[IMDB_RATING] and tvSerie["name"] < heighest_rated_serie[NAME]):
                    heighest_rated_serie = (tvSerie["name"], tvSerie["imdb_rating"])

    if heighest_rated_serie[IMDB_RATING] == IMDB_RATING_SERIES_NOT_FOUND:
        raise SeriesNotFoundException("Either no the series belongs to that genre, or the genre does not exists.")

    return heighest_rated_serie[NAME]

def main():
    print(bestInGenre('Actio'))

main()