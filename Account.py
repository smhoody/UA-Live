"""
    Account class used to store info about twitter accounts

@author Steven Hoodikoff
@date 02/27/2022
"""

class Account(object):
    """ Represents a Twitter account """
    def __init__(self,id, username, tweet="", time=""):
        """ Constructor to initialize an account with ID and username """
        self.id = id
        self.username = username
        self.tweet = tweet
        self.time = time

    def get_id(self):
        """Return the id of the account (int)"""
        return self.id

    def get_username(self):
        """Return the username of the account (includes '@')"""
        return self.username

    def get_tweet(self):
        """Returns the latest tweet of the account (string)"""
        return self.tweet

    def get_time(self):
        """Returns the time of the latest tweet (string)"""
        return self.time

    def set_username(self, username):
        """Set the username"""
        self.username = username

    def set_tweet(self, tweet):
        """Set the latest tweet"""
        self.tweet = tweet

    def set_time(self, time):
        """Set the latest tweet time"""
        self.time = time

    def __str__(self):
        """Returns the username, latest tweet, and time of tweet"""
        return f"{self.username}\n{self.time}\n{self.tweet}"