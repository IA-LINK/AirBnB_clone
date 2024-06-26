#!/usr/bin/python3

import unittest
from models import City
from datetime import datetime
import os


class TestCityModel(unittest.TestCase):
    def setUp(self):
        self.city_model = City()

    def tearDown(self):
        del self.city_model

    def test_instance_creation(self):
        self.assertIsInstance(self.city_model, City)
        self.assertTrue(hasattr(self.city_model, 'id'))
        self.assertTrue(hasattr(self.city_model, 'created_at'))
        self.assertTrue(hasattr(self.city_model, 'updated_at'))
        self.assertTrue(hasattr(self.city_model, 'state_id'))
        self.assertTrue(hasattr(self.city_model, 'name'))

    def test_string_representation(self):
        string_repr = str(self.city_model)
        self.assertIn("[City]", string_repr)
        self.assertIn("id", string_repr)
        self.assertIn("created_at", string_repr)
        self.assertIn("updated_at", string_repr)
        self.assertIn("state_id", string_repr)
        self.assertIn("name", string_repr)

    def test_to_dict_method(self):
        city_dict = self.city_model.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIn('id', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertIn('state_id', city_dict)
        self.assertIn('name', city_dict)


if __name__ == '__main__':
    unittest.main()