import unittest

#from flask import Flask
from app import myapp_obj
#from app.routes
from . import myapp_obj
from ..models import User


class MyTestCase(unittest.TestCase):
    # Testing the creation of new user
    def test_new_user(self):
        myapp_obj.run(debug = True)
        new_user = User(username="Bobby", password="1234")
        self.assertEquals(new_user.username, "Bobby")

    def test_delete_user(self):
        pass

if __name__ == '__main__':
    unittest.main()
