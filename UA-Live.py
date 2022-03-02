"""
	Get live updates (every min) from Twitter about Ukraine-Russia conflict

@author Steven Hoodikoff
@date 02/27/2022

Currently Used Twitter accounts and their IDs:
@KyivIndependent    : 1462548977367359490
@MFA_Ukraine        : 143427448
@Ukraine            : 732521058507620356
@Ukraine_World      : 873135988440223745
@ZelenskyyUa        : 1120633726478823425
@UKRINFORM          : 167317309
@FedorovMykhailo    : 1331528215899344896
@EuromaidanPress    : 2595088842
@NewVoiceUkraine    : 1483388011371016195
@mrsorokaa          : 1091409575343992832
@IAPonomarenko      : 262219168
@ua_industrial      : 435239369
to add more accounts, add it to the json file in util
"""
import tweepy, time
import json
#local
from Account import Account

WOEIDS = {"ukraine":23424976, "kyiv":924938, "donetsk":919163, "lviv":924943}


def tweet_update(api, accounts):
    """
    Retreive updated twitter account info and print for each account

    :param api: (API object from tweepy)
    :param accounts: (list of Account objects)
    """
    while True:
        for account in accounts:
            twitter_account = api.get_user(user_id=account.get_id())
            try:
                tweet = twitter_account.status
            except AttributeError: #Wrong object will be returned from get_user if there is a problem with the ID
                print("Could not retrieve tweet from account ID", account.get_id())
            else:
                if (account.get_tweet() != tweet.status.text): #essentially makes sure it doesnt print if there isnt a new tweet
                    account.set_tweet(tweet.status.text)
                    account.set_time(est_convert(tweet.status.created_at))

                    print("\n\n", account.get_username(), "\n", account.get_time(), "\n", account.get_tweet())
                    retweet(api, twitter_account.status)
        
        time.sleep(60)  # 1 minute pause


def retweet(api, tweet):
    """ 
    Retweets the given tweet
    :param api: (API object from tweepy)
    :param tweet: (Status object from tweepy)
    """
    try:
        api.retweet(tweet.id)
    except:
        print(f"Error - Could not retweet:\n{tweet.id}\n{tweet.text}")


def get_account_info():
    """ Create Account objects to save the info about each Twitter account, return list """
    with open('util/accounts.json', 'r') as file:
        account_ids = json.load(file)

    accounts = []
    for name, id in account_ids.items():
        accounts.append(Account(id, name))

    return accounts


def est_convert(time):
    """
    Converts the time from UTC to EST

    :param Time: (string from KYIV_INDEPENDENT_ACC.status.created_at)
    :return: (string with date and time in EST)
    """
    status_datetime = str(time).split(" ")
    EST_hour = int(status_datetime[1][0:2]) - 5 #change 5 hours behind
    status_time = status_datetime[1].split(":")[0:3]
    status_time[0] = EST_hour
    new_time = ":".join(map(str, status_time))
    status_datetime[1] = new_time
    status_datetime.append("EST")
    return " ".join(status_datetime)


def get_auth():
    """ Get authorization to @CobeDot from Twitter """
    with open("util/credentials.json") as file:
        creds = json.load(file)

    auth = tweepy.OAuthHandler(creds["consumer key"], creds["consumer secret"])
    auth.set_access_token(creds["access key"], creds["access secret"])

    return tweepy.API(auth)



def main():
    api = get_auth()
    tweet_update(api, get_account_info())



if __name__ == "__main__":
    main()
