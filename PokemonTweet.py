from bs4 import BeautifulSoup
import requests


def pokemon_tweet(howManyPosts):
  page = "pokemon"
  messages = set()
  while True:
    res = requests.get('https://twitter.com/'+ page)
    bs = BeautifulSoup(res.content, 'lxml')
    all_tweets = bs.find_all('div', {'class': 'tweet'})
    if all_tweets:
      for tweet in all_tweets[:howManyPosts]:
        context = tweet.find('div', {'class': 'context'}).text.replace("\n", " ").strip()
        content = tweet.find('div', {'class': 'content'})
        message = content.find('div', {'class': 'js-tweet-text-container'}).text.replace("\n", " ").strip()

        if message not in messages:

          return message
          #print()
        messages.add(message)
    else:
      print("List is empty/account name not found.")


howManyPosts = 1   #This is pretty self-explanatory, it means how many posts you want to print

pokemon_tweet(howManyPosts)
