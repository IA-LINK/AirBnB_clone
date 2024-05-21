#!/bin/python3 

import unittest
from models.user import User
from models.engine import file_storage  

class TestUser(unittest.TestCase):

  def setUp(self):
    
    file_storage.delete("User.test_user1")
    file_storage.delete("User.test_user2")

  def test_user_creation(self):
  
    user = User(email="test@example.com", password="test123", first_name="John", last_name="Doe")
    
    file_storage.save(user)
   
    loaded_user = file_storage.load("User." + user.id)
   
    self.assertEqual(loaded_user.email, user.email)
    self.assertEqual(loaded_user.password, user.password)  # Consider password hashing for security
    self.assertEqual(loaded_user.first_name, user.first_name)
    self.assertEqual(loaded_user.last_name, user.last_name)

  def test_user_update(self):
 
    user = User(email="test@example.com", password="test123", first_name="John", last_name="Doe")
    file_storage.save(user)
   
    user.first_name = "Jane"
   
    file_storage.save(user)
    
    loaded_user = file_storage.load("User." + user.id)
   
    self.assertEqual(loaded_user.first_name, "Jane")
    self.assertEqual(loaded_user.last_name, "Smith")


if __name__ == '__main__':
  unittest.main()
