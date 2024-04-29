#!/usr/bin/python3

"""
This module demonstrates the first step in using SQLAlchemy
 for ORM (Object-Relational Mapping).
It defines a simple SQLAlchemy model
for a 'states' table and sets up the database connection.

Usage:
    python3 6-model_state.py <username> <password> <database_name>

This script creates a 'states' table in the specified MySQL database
 with two columns:
- 'id': An auto-incrementing integer serving as the primary key.
- 'name': A string column that cannot be null.

The script uses SQLAlchemy's declarative base system to
define the 'State' model and
creates the table in the database.

Requirements:
    - Python 3.x
    - SQLAlchemy
    - MySQL server

Author: Foash
Date: 2024-04-15
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    Represents the 'states' table in the database.

    Attributes:
        id (int): An auto-incrementing integer serving as the primary key.
        name (str): A string column that cannot be null.
    """

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    city = relationship("City", back_populates='state')
