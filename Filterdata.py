
import csv
import re
import pygal as pg

def main(tweets, member_dict):
    """
    This is the function that ties every function to work together
    """
    with open('bnkdata.csv', encoding='utf-8') as csvfile: #chang your path
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
    #print(sum(member_dict.values())) use this to check how many tweets
    member_dict = sort_members_data(member_dict)
    member_dict = filter_member_data(member_dict)
    #===============Render chart====================
    chart_horizontal = pygal_horizontal(member_dict)
    chart_pie = pygal_pie(member_dict)
    chart_horizontal.render_to_file('BNK48graph top 7.svg')
    chart_pie.render_to_file('BNK48graph all member.svg')
    #===============================================
    #print("\n".join([(i + " = " + str(member_dict[i])) for i in member_dict.keys()])) check member dcit easy format
    #print(member_dict) check member_dict
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
    if check_hashtags(hashtags) != []:
        return check_hashtags(hashtags)

def check_hashtags(hashtags):
    """ Check if hashtag include BNK48"""
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

def  filter_member_data(data):
    """ Filter member """
    member_dict = {}
    member_list = ['#mobilebnk48', '#cherprangbnk48', '#weebnk48', '#kaewbnk48','#noeybnk48','#ornbnk48', \
    '#fondbnk48', '#punbnk48', '#mewnichbnk48', '#jennisbnk48', '#musicbnk48', '#myyubnk48', '#satchanbnk48', \
    '#kornbnk48', '#kaimookbnk48', '#janebnk48', '#jibbnk48', '#mindbnk48', '#oombnk48', '#mioribnk48', '#pupebnk48', \
    '#nikybnk48', '#newbnk48', '#namneungbnk48', '#junebnk48', '#izurinabnk48', '#natherinebnk48', '#viewbnk48', \
    '#tarwaanbnk48', '#minminbnk48', '#cakebnk48', '#aombnk48', '#ratahbnk48', '#phukkhombnk48', '#khaminbnk48', \
    '#stangbnk48', '#pandabnk48', '#ninebnk48', '#namsaibnk48', '#khengbnk48', '#fifabnk48', '#faiibnk48', '#jaabnk48', \
    '#piambnk48', '#mairabnk48', '#deeneebnk48', '#gygeebnk48', '#pakwanbnk48', '#bamboobnk48', '#ninkbnk48', '#katebnk48']
    for hashtag in data:
        if hashtag in member_list:
            member_dict[hashtag] = data[hashtag]
    return member_dict

def pygal_horizontal(data):
    """made horizontal chart"""
    data_tuple = sorted(data.items() , reverse=True, key=lambda x: x[1])
    line_chart = pg.HorizontalBar()
    line_chart.title = 'Top 7 BNK48 member'
    for i in range(0,7):
        line_chart.add(data_tuple[i][0], data_tuple[i][1])
    return line_chart

def pygal_pie(data):
    """made pie chart"""
    data_tuple = sorted(data.items() , reverse=True, key=lambda x: x[1])
    pie_chart = pg.Pie()
    pie_chart.title = 'All BNK48 member #hashtag'
    for i in range(0,51):
        pie_chart.add(data_tuple[i][0], data_tuple[i][1])
    return pie_chart

main('', {})
