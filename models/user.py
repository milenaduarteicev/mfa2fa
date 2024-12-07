# models/user.py
class User:
    def __init__(self, id, username, password, otp_secret=None):
        self.id = id
        self.username = username
        self.password = password
        self.otp_secret = otp_secret

    def get_id(self):
        return self.id
