#!/usr/bin/python3

from unittest import TestCase
from models.user import User
from manager import Manager

class TestManager(TestCase):
  def setUp(self):
    self.manager = Manager()

  def test_create(self):
    user_data = {"email": "bob@example.com", "first_name": "Bob", "last_name": "Jones"}
    self.manager.create(1, user_data)
    user = self.manager.get(1)
    self.assertEqual(user.email, user_data["email"])

  def test_create_duplicate(self):
    user_data = {"email": "alice@example.com", "first_name": "Alice"}
    self.manager.create(1, user_data)
    with self.assertRaises(KeyError):
      self.manager.create(1, user_data)  # Should raise error for duplicate ID

  def test_get_existing(self):
    user_data = {"email": "alice@example.com", "first_name": "Alice"}
    self.manager.create(1, user_data)
    user = self.manager.get(1)
    self.assertEqual(user.email, user_data["email"])

  def test_get_nonexistent(self):
    with self.assertRaises(KeyError):
      self.manager.get(2)

  def test_update(self):
    user_data = {"email": "alice@example.com", "first_name": "Alice"}
    self.manager.create(1, user_data)
    update_data = {"last_name": "Smith"}
    self.manager.update(1, update_data)
    user = self.manager.get(1)
    self.assertEqual(user.last_name, update_data["last_name"])

  def test_update_nonexistent(self):
    with self.assertRaises(KeyError):
      self.manager.update(2, {"first_name": "Bob"})

  def test_destroy(self):
    user_data = {"email": "alice@example.com", "first_name": "Alice"}
    self.manager.create(1, user_data)
    self.manager.destroy(1)
    with self.assertRaises(KeyError):
      self.manager.get(1)

  def test_destroy_nonexistent(self):
    with self.assertRaises(KeyError):
      self.manager.destroy(2)

  def test_show_all(self):
    user_data1 = {"email": "alice@example.com", "first_name": "Alice"}
    user_data2 = {"email": "bob@example.com", "first_name": "Bob"}
    self.manager.create(1, user_data1)
    self.manager.create(2, user_data2)
    output = self.captureStdOut(lambda: self.manager.show())
    self.assertIn(user_data1["email"], output.getvalue())
    self.assertIn(user_data2["email"], output.getvalue())