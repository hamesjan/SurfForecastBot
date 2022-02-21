from socket import SOL_UDP
import tweepy
import requests
from bs4 import BeautifulSoup
from config import ACCESS_TOKEN, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET;

def main():
    # auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    # auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # # Create API object
    # api = tweepy.API(auth)


    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    job_elements = soup.find_all("div", class_="card-content")
    for job_element in job_elements:
        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")
        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location_element.text.strip())
        print()

    

    # Create a tweet
    # api.update_status("Hello Tweepy")
    # print("ok")

if __name__ == "__main__":
    main()
