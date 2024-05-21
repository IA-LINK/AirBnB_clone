#!/bin/python3 

from unittest import TestCase
from models.user import User

class TestUser(TestCase):
  def test_init(self):
    user = User(email="alice@example.com", first_name="Alice", last_name="Smith")
    self.assertEqual(user.email, "alice@example.com")
    self.assertEqual(user.first_name, "Alice")
    self.assertEqual(user.last_name, "Smith")

  def test_validator_email_empty(self):
    with self.assertRaises(ValueError):
      User(email="")

  def test_validator_email_invalid(self):
    with self.assertRaises(ValueError):
      User(email="invalid_email")
