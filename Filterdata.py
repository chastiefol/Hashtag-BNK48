
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
                    for hashtag in count_hashtags(tweets):
                        if hashtag not in member_dict:
                            member_dict[hashtag] = 1
                        else:
                            member_dict[hashtag] += 1
    #print(sum(member_dict.values())) check how many tweets
    member_dict = sort_members_data(member_dict)
    print("\n".join([(i + " = " + str(member_dict[i])) for i in member_dict.keys()]))

def removeRT(tweet):
    """
    Remove the data if data is a retweets
    """
    if "RT" not in tweet[0:3]:
        return tweet.lower()

def count_hashtags(tweet):
    """
    Check how many tweet with members hashtags
    """
    hashtags = (re.findall(r"\B(\#[a-zA-Z0-9]+\b)(?!;)", tweet))
    if filter_hashtag(hashtags) != []:
        return filter_hashtag(hashtags)

def filter_hashtag(hashtags):
    """ Check if hashtag include BNK48"""
    # print('=============================================')
    # print(hashtags)
    ["#iknon", "#bnk48"]
    payload = []
    for hashtag in hashtags:
        if hashtag[-5:] == 'bnk48' and hashtag != '#bnk48':
            payload.append(hashtag)
    return payload

def sort_members_data(data):
    """
    Sort member data
    """
    sort_data = sorted((value, key) for (key,value) in data.items())
    members = {}
    for member in sort_data[::-1]:
        members[member[1]] = member[0]
    return members

main('', {})
