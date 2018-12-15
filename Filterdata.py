
import csv
import re

def main(tweets, member_dict):
    """
    This is the function that ties every function to work together
    """
    with open('bnkdata.csv', encoding='utf-8') as csvfile:
        for data in csvfile:
            data = data.split(',')
            if removeRT(data[1]) != None: # Check if data is not None
                tweets = removeRT(data[1])

                if count_hashtags(tweets) != None: # Check Hashtags
                    if count_hashtags(tweets) not in member_dict:
                        member_dict[count_hashtags(tweets)] = 1
                    else:
                        member_dict[count_hashtags(tweets)] += 1
    #print(sum(member_dict.values())) check how many tweets

def removeRT(tweet):
    """
    Remove the data if data is a retweets
    """
    if "RT" not in tweet[0:3]:
        return tweet.capitalize()


def count_hashtags(tweet):
    """
    Check how many tweet with members hashtags
    """
    tweet = (re.findall(r"\B(\#[a-zA-Z0-9]+\b)(?!;)", tweet))
    for hashtag in tweet:
        return hashtag


main('', {})
