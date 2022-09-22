from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from api import crud, schema
from api.database import create_database, get_db

create_database()
app = FastAPI()


@app.get(
    "/intervals",
    tags=["intervals"],
    summary="Min and Max award winning intervals",
    description="""Returns producers with smallest and
                biggest interval between winning 2 awards.""",
    response_model=schema.WinnerIntervals,
)
def min_max_intervals(db: Session = Depends(get_db)):
    """Get min and max intervals between winning 2 awards

    Args:
        db (Session): SQLAlchemy session DB. Defaults to Depends(get_db).

    Returns:
        schema.WinnerIntervals: Dict of lists of min and max producers.
    """
    return crud.select_min_max_intervals(db)
