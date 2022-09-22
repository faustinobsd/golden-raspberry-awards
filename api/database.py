import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

# Create a new instance of SQLite in memory
engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

CSV_FILE = "data/movielist.csv"


def get_db():
    """
    Get a SQLAlchemy Session

    :return: SQLAlchemy Session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_database():
    """
    Creates a new SQLite database from the CSV
    data file.

    :return: None
    """
    Base.metadata.create_all(bind=engine)
    df = _get_dataframe_for_db()

    try:
        with engine.begin() as connection:
            df.to_sql(
                "movielist", con=connection, index=False, if_exists="append"
            )
    except SQLAlchemyError as e:
        print("Failed to create SqlAlchemy database!", e)
        raise
    else:
        print("Database successfully created.")


def _get_dataframe_for_db():
    """
    Reads the CSV_FILE, parses it to a
    Pandas dataframe and fit to our Data Model

    :return: Pandas DataFrame
    """
    df = pd.read_csv(CSV_FILE, sep=";")

    # Split multiple producers into new rows in the dataframe
    new_df = df.assign(
        producers=df["producers"].str.split(r", and |, | and ")
    ).explode("producers")

    return new_df
