import json
import os
import re
from random import random, randrange, randint

import tweepy
from nltk import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize
from tweepy.auth import OAuthHandler


# Authenticate to Twitter


def get_random_verb(stuff, pos):
    random_number = randrange(len(stuff[pos[1]]))
    counter = 0
    for i in range(0, len(stuff[pos[1]])):
        if counter == random_number:
            return stuff[pos[1]][i]
        counter += 1


def get_random_noun(stuff, pos):
    random_number = randrange(len(stuff[pos[1]]))
    counter = 0
    for i in range(0, len(stuff[pos[1]])):
        if counter == random_number:
            return stuff[pos[1]][i]
        counter += 1


def main():
    auth = OAuthHandler(os.environ.get('API_KEY'), os.environ.get('API_SECRET_KEY'))
    auth.set_access_token(os.environ.get('ACCESS_TOKEN'),
                          os.environ.get('ACCESS_SECRET_TOKEN'))

    # # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True)
    with open('verbs-tagged.json', 'r+') as out_json:
        verb_data = json.load(out_json)
        # for word in data:
        #     print(data[word][0][0][1])

    with open('nouns-tagged.json', 'r+') as out_json:
        noun_data = json.load(out_json)
        # for word in data:
        #     print(data[word][0][0][1])

    # Create a tweet
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    with open('new-tweets.txt', 'w') as output_text:
        timeline = api.home_timeline(count=20, tweet_mode="extended")
        for tweet in timeline:
            full_tweet = str(tweet.full_text)
            full_tweet = full_tweet.replace("&amp;", "&")
            text = word_tokenize(tweet.full_text)
            new_text = pos_tag(text)
            new_tweet = ""
            output_text.write(tweet.full_text + "\n\n")
            for pos in new_text:
                if pos[0] == "https":
                    break
                if len(pos[0]) == 1:
                    continue
                rand_num = randint(1, 5)
                if True:
                    if pos[1] == "VB" or pos[1] == "VBG" or pos[1] == "VBN":
                        random_verb = get_random_verb(verb_data, pos)
                        full_tweet = full_tweet.replace(str(pos[0]), str(random_verb), 1)
                        continue
                    if pos[1] == "NN" or pos[1] == "NNS":
                        random_noun = get_random_noun(noun_data, pos)
                        full_tweet = full_tweet.replace(str(pos[0]), str(random_noun), 1)
                        continue
                new_tweet += pos[0] + " "
            # api.update_status(new_tweet)
            output_text.write("******" + full_tweet + "\n\n")
            # output_text.write(new_tweet + "\n\n\n\n")


if __name__ == "__main__":
    main()
