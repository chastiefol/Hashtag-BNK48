# Hashtag-BNK48

ศึกษาและวิเคราะห์ข้อมูล # ในทวิตเตอร์ว่า เมมเบอร์คนใหนใน BNK48 ถูกกล่าวถึงมากที่สุด ในช่วงหนึ่งอาทิตย์ (7-14 ธันวาคม 2561)


### Requirement
โปรแกรมและ Module ที่ใช้
```
Python3
Tweepy
Pandas
Pygal
```

### เริ่มต้นกันเลย

ก่อนอื่นเรามาเรื่มรันตัว Streaming script ของเรากันก่อนเลย
เราเริ่มต้นโดยการรัน streamingTwitter.py กันก่อน
<<<<<<< HEAD
```
# Import modules
import tweepy
import json
import csv

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, tweet):
        """ Import streaming text to CSV """
        with open('bnkdata.csv', 'a', encoding='utf-8',  newline='') as writeFile:
            payload = [tweet.created_at, tweet.text.replace('\n', ' ')]
            writer = csv.writer(writeFile)
            writer.writerow(payload)
            print(sum(1 for line in csv.reader( open('bnkdata.csv', 'r', encoding='utf-8'))))

def main ():
    """ Create credential variables"""
    consumer_key = 'your_consumer_key'        # put your consumer_key from Twitter API
    consumer_secret = 'your_consumer_secret'  # put your consumer_secret from Twitter API
    access_token = 'your_access_token'        # put your access_token from Twitter API
    access_secret = 'your_access_secret'      # put your access_secret from Twitter API

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    api = tweepy.API(auth)

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
    myStream.filter(track=['#BNK48'])

main()

```
=======
โดยจะต้องใส่ Key API ของ Twitter ลงไปเองด้วยจ้ท ทางเราให้ไม่ได้ TT

หลังรันไปสักพัก เราจะเห็นตัวเลขขึ้นมามากมาย นั่นหมายถึงจำนวนข้อมูลที่เรา Stream มาได้นะจ้ะ รูปที่แคปมาคือรันต่อจากไฟล์อันเก่านะจ้ะ มันเลยเป็น 6 หมื่นกว่าข้อมูล
<img src='README/Streamtest.jpeg'>


## Contributing

|<img src="README/nanapoou.jpg" width="150px" height="150px">|<img src="README/Paweennuch.jpg" width="150px" height="150px">|<img src="README/SuraweeTedsakorn.jpg" width="150px" height="150px">|<img src="README/chastiefol.jpg" width="150px" height="150px">|
|:-----:|:-----:|:-----:|:-----:|
|[nanapoou](https://github.com/nanapoou)|[Paweennuch](https://github.com/Paweennuch)|[SuraweeTedsakorn](https://github.com/SuraweeTedsakorn)|[chastiefol](https://github.com/chastiefol)|
#### Member list
- นาย นายนวภูมิ แก้วมณี 61070102
- นางสาว ปวีณนุช ตุ้ยใหม่ 61070120
- นาย นายสุรวีร์ เทศกรณ์ 61070252
- นาย กันต์ วงษ์อุบล 61070337
