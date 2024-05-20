#!/usr/bin/python3

import uuid

from datetime import datetime

class BaseModel:
    """Definition of a the class BaseModel."""
    """This class is inherited from BaseModel including the
    various attributes."""
    """It also inherits the following public class attributes:
    - attributes = {} a dict attribute.
    """

    def __init__(self, *args, **kwargs):
        """Initialization of a new BaseModel Instance.
        Args remains unused."""

        if kwargs:
            for entry, value in kwargs.items():
                if entry == "created_at" or entry == "updated_at":
                    setattr(self, entry, datetime.fromisoformat(value))
                elif entry != "__class__":
                    setattr(self, entry, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """This returns a string representation of the BaseModel instance."""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """This updates the updated_at attribute with the current date and time."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """A dictionary is returned containing all the possible
        keya/vaues of the __dict__ instance."""

        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
