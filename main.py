#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import snscrape.modules.twitter as sntwitter


# In[2]:

print("Welcome To The Tweet Like Sorter")
print("A csv file will be written in the current directory")
query = str(input("Insert user to sort: "))
# query = "elonmusk"
scraper = sntwitter.TwitterUserScraper(query)


# In[ ]:


tweets = []
i = 0
maxrange = int(input("Insert Max Number Of Tweets to find: "))
for tweet in scraper.get_items():
    if query in tweet.user.username:
        data = [
            tweet.user.username,  tweet.id, tweet.likeCount,  tweet.date,  tweet.content, tweet.url]
        
        tweets.append(data)
        i += 1
        print(f"I have found {i}/{maxrange} Tweets" )
            


    if i == maxrange:
        tweets.pop()
        break


# In[ ]:


df = pd.DataFrame(tweets)
df.columns = ["Username","Id","Likes","Date","Content","URL"]

sortedf = df.sort_values("Likes",ascending=False)
sortedf.to_csv(f"{query}-last-{maxrange}-tweets ordered by likes.csv")

print("Csv Written!!")
first = sortedf['URL'].iloc[:1]
print(f"Here's the Link to The Most liked Tweet from the last {maxrange} tweets")
print(str(first.values))