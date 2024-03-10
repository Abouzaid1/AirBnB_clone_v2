#!/usr/bin/python3
"""
Defines the state model
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Blueprint for City objects
    """
    state_id = ""
    name = ""
