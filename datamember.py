import csv
import pandas as pd
def getCSV():
    """get csv function"""
    csvdf = pd.read_csv('C:/Users/WIN/Desktop/Project PSIT2/bnkdata.csv', encoding='utf-8')
    columns = ["date","text"]
    csvdf.columns = columns
    text = csvdf['text']
    return text

def RemoveRT():
    """Remove "RT" function"""
    text = getCSV()
    lit = []
    count = 1
    for i in text:
        if i[0:2] == "RT":
            pass
        else:
            lit.append(i.lower())
    return lit

def countmember():
    """Count BNK member function"""
    data = RemoveRT()
countmember()
