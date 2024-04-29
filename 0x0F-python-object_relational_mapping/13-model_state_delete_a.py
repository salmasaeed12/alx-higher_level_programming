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

    deleted_A_states = session.query(State).\
        filter(State.name.like('%a%')).all()

    for state in deleted_A_states:
        session.delete(state)
        # session.delete() only can delete one record a time
    session.commit()

    session.close()
