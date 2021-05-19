from flask import Flask
#from app.routes
from CMPE131TEAM6.app.models import User


class MyTestCase(unittest.TestCase):
    # Testing the creation of new user
    def test_new_user(self):
        app = Flask(__name__)
        new_user = User(username="Bobby", password="1234")
        self.assertEquals(new_user.username, "Bobby")


if __name__ == '__main__':
    unittest.main()
