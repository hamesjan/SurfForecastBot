import tweepy;
import config.py;


def main():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Create API object
    api = tweepy.API(auth)

    # Create a tweet
    api.update_status("Hello Tweepy")
    print("ok")

if __name__ == "__main__":
    main()
