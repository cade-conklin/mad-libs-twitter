import json
from random import random, randrange

import tweepy
from nltk import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize
from tweepy.auth import OAuthHandler

# Authenticate to Twitter
auth = OAuthHandler("C2n5gEgvpTp9wjryQ1lvZm64k", "Oqs68NjaNqHQ0R5KHLDNLOkrRt5VOAlKRVAp5U7Fff4XViaAcr")
auth.set_access_token("1290484030756909060-OOOHsb5YCWqT2KYjPZDuezVtNCcyv0",
                      "FScH0OukIM5FYobmUrlNkNulwj5ghkQ3VK4DFnZNfwubx")


# # Create API object
api = tweepy.API(auth, wait_on_rate_limit=True)
data = dict()
with open('verbs-dictionaries.json') as verb_json:
    data = json.load(verb_json)



# API Key#C2n5gEgvpTp9wjryQ1lvZm64k
# API Secret Key #Oqs68NjaNqHQ0R5KHLDNLOkrRt5VOAlKRVAp5U7Fff4XViaAcr
# Bearer Token
# #AAAAAAAAAAAAAAAAAAAAAHw1GgEAAAAA4KxhRXaOin0XfyuXYJAT%2FIkG51M%3DOPDstJThhwB28CUkwXkFKLGnShvMg1bl0nOueiZ8Y5cWx0jWsi
# ACcess token
# 1290484030756909060-OOOHsb5YCWqT2KYjPZDuezVtNCcyv0
# Access Secret token
# FScH0OukIM5FYobmUrlNkNulwj5ghkQ3VK4DFnZNfwubx
# Create a tweet
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

with open('new-text.txt', 'w') as output_text:
    timeline = api.home_timeline(tweet_mode="extended")
    for tweet in timeline:
        # print(f"{tweet.user.name} said {tweet.text}")
        text = word_tokenize(tweet.full_text)
        new_text = pos_tag(text)
        new_tweet = ""
        output_text.write(tweet.full_text + "\n\n")
        for pos in new_text:
            if pos[1] == "VB" or pos[1] == "VBG" or pos[1] == "VBD" or pos[1] == "VBN" or pos[1] == "VBP" or pos[1] == "VBZ":
                random_number = randrange(len(data))
                random_verb = data[random_number][1]
                new_tweet += random_verb + " "
                continue
            new_tweet += pos[0] + " "
        output_text.write(new_tweet + "\n\n\n\n")

# user = api.get_user("spence_temp")
#
# print("User details:")
# print(user.name)
# print(user.description)
# print(user.location)
# print(user.text)
#
# print("Last 20 Followers:")
# for follower in user.followers():
#     print(follower.name)
# print(user.status())
