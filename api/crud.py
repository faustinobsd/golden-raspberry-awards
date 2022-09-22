"""
    CRUD operations for the API.
    Implemented only one GET as stated on test specification.
"""

from sqlalchemy.orm import Session

from api.models import Movie


def select_min_max_intervals(db: Session):
    """
    Obter o produtor com maior intervalo entre dois prêmios consecutivos,
    e o que obteve dois prêmios mais rápido, seguindo a especificação de
    formato definida na página 2.
    """
    min_interval = 999
    max_interval = 0
    last_producer = {"producer": "", "year": 0}
    duplicate_winners = []

    query = (
        db.query(Movie)
        .filter(Movie.winner == "yes")
        .order_by(Movie.producers, Movie.year)
        .all()
    )

    for row in query:
        if last_producer["producer"] == row.producers:
            interval = row.year - last_producer["year"]
            result_dict = {
                "producer": row.producers,
                "interval": interval,
                "previousWin": last_producer["year"],
                "followingWin": row.year,
            }

            if interval >= max_interval:
                max_interval = interval

            if interval <= min_interval:
                min_interval = interval

            duplicate_winners.append(result_dict)

        last_producer["producer"] = row.producers
        last_producer["year"] = row.year

    min_max_intervals = {
        "min": [
            d for d in duplicate_winners if d.get("interval") == min_interval
        ],
        "max": [
            d for d in duplicate_winners if d.get("interval") == max_interval
        ],
    }

    return min_max_intervals
