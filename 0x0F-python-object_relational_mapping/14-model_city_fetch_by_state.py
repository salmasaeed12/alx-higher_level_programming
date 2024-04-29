#!/usr/bin/python3

"""
import class State and city and do quering with join on them
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv


if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    _Session = sessionmaker(bind=engine)
    session = _Session()

    rows = session.query(State, City).filter(State.id == City.state_id)\
        .order_by(City.id).all()

    for row in rows:
        print("{}: ({}) {}".format(row.State.name, row.City.id, row.City.name))
