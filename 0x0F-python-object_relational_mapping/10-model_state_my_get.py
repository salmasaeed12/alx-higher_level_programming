#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
        )

    _Session = sessionmaker(bind=engine)
    session = _Session()

    rows = session.query(State).order_by(State.id).all()
    """
    The all() method in SQLAlchemy returns a list of results,
    and you should apply the order_by
    method to the query object before calling all()
    to ensure that the ordering is applied correctly
    before calling all() to retrieve the results.
    """

    flag = 0
    for row in rows:
        if row.name == sys.argv[4]:
            print(row.id)
            flag = 1

    if flag == 0:
        print("Not found")
