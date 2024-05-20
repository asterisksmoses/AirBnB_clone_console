#!/usr/bin/python3

import unittest

from models.base_model import BaseModel

from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """This is a unittest for the BaseModel class."""

    def test_init(self):
        """Initializes the test process for the BaseModel."""
        base_model = BaseModel()
        self.assertIsNotNone(base_model.id)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_str(self):
        """This initializes the test process for the string representation of a
        BaseModel instance."""
        base_model = BaseModel()
        req_str = f'[{base_model.__class__.__name__}] ({base_model.id}) {base_model.__dict__}'
        self.assertEqual(str(base_model), req_str)

    def test_save(self):
        """This is the test case for the save part of the BaseModel instance."""
        base_model = BaseModel()
        new_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(new_updated_at, base_model.updated_at)

    def test_to_dict(self):
        base_model = BaseModel()
        expc_dict = base_model.to_dict()
        self.assertEqual(expc_dict['__class__'], 'BaseModel')
        self.assertEqual(expc_dict['id'], base_model.id)
        self.assertEqual(expc_dict['created_at'], base_model.created_at.isoformat())
        self.assertEqual(expc_dict['updated_at'], base_model.updated_at.isoformat())

    def test_from_dict(self):
        base_model = BaseModel()
        expc_dict = base_model.to_dict()
        curr_model = BaseModel(**expc_dict)
        self.assertEqual(curr_model.id, base_model.id)
        self.assertEqual(curr_model.created_at, base_model.created_at)
        self.assertEqual(curr_model.created_at, base_model.created_at)
        self.assertEqual(curr_model.updated_at, base_model.updated_at)

if __name__ == "__main__":
    unittest.main()
