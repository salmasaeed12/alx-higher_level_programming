#!/usr/bin/python3

"""
import class State and city and do quering with join on them
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    _Session = sessionmaker(bind=engine)
    session = _Session()

    california = State(name="California")
    session.add(california)
    session.commit()
    san = City(name="San Francisco", state_id=california.id)
    session.add(san)
    session.commit()

    states = session.query(State).all()
    cities = session.query(City).filter(State.id == City.state_id).all()

    session.close()
