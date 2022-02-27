"""
    Account class used to store info about twitter accounts
"""

class Account(object):
    def __init__(self,id, username, tweet="", time=""):
        self.id = id
        self.username = username
        self.tweet = tweet
        self.time = time

    def get_id(self):
        return self.id

    def get_username(self):
        return self.username

    def get_tweet(self):
        return self.tweet

    def get_time(self):
        return self.time

    def set_username(self, username):
        self.username = username

    def set_tweet(self, tweet):
        self.tweet = tweet

    def set_time(self, time):
        self.time = time

    def __str__(self):
        return f"{self.username}\n{self.time}\n{self.tweet}"