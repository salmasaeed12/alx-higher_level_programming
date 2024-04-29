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

    updated_state = session.query(State).filter(State.id.like(2)).first()
    updated_state.name = 'New Mexico'
    session.add(updated_state)
    session.commit()

    session.close()
