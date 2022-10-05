from django.test import TestCase
from . import models

"""
A User should store...
- A unique ID
- A first name (CharField(max_length=32))
- A last name (CharField(max_length=32))
- A username (CharField(max_length=32))
- A bio (CharField(max_length=200))
"""
class UserTest(TestCase):
    def setup(self): 
        pass




    
