#!/usr/bin/python3

import unittest
from models import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_storage = FileStorage()

    def tearDown(self):
        del self.file_storage
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_method(self):
        objects_dict = self.file_storage.all()
        self.assertIsInstance(objects_dict, dict)
        self.assertEqual(objects_dict, self.file_storage._FileStorage__objects)

    def test_new_method(self):
        new_object = BaseModel()
        self.file_storage.new(new_object)
        key = "{}.{}".format(new_object.__class__.__name__, new_object.id)
        self.assertIn(key, self.file_storage._FileStorage__objects)
        self.assertEqual(
            self.file_storage._FileStorage__objects[key],
            new_object
        )

    def test_save_and_reload_methods(self):
        # Create and save objects
        obj1 = BaseModel()
        obj2 = User()
        obj3 = State()
        self.file_storage.new(obj1)
        self.file_storage.new(obj2)
        self.file_storage.new(obj3)
        self.file_storage.save()

        # Check if the file is created
        self.assertTrue(os.path.exists("file.json"))

        # Clear the objects in memory
        del self.file_storage._FileStorage__objects

        # Reload the objects from the file
        self.file_storage.reload()

        # Check if the reloaded objects match the original ones
        key1 = "{}.{}".format(obj1.__class__.__name__, obj1.id)
        key2 = "{}.{}".format(obj2.__class__.__name__, obj2.id)
        key3 = "{}.{}".format(obj3.__class__.__name__, obj3.id)

        self.assertIn(key1, self.file_storage._FileStorage__objects)
        self.assertIn(key2, self.file_storage._FileStorage__objects)
        self.assertIn(key3, self.file_storage._FileStorage__objects)
        self.assertEqual(
            self.file_storage._FileStorage__objects[key1].to_dict(),
            obj1.to_dict()
        )
        self.assertEqual(
            self.file_storage._FileStorage__objects[key2].to_dict(),
            obj2.to_dict()
        )
        self.assertEqual(
            self.file_storage._FileStorage__objects[key3].to_dict(),
            obj3.to_dict()
        )


if __name__ == '__main__':
    unittest.main()