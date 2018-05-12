import twitter
import sqlite3
import time
from time import strftime, localtime
import random
import re
import sys

api = 0
COUNT = 50
deleted = 0

def Login():
    global api
    api = twitter.Api(consumer_key='idhfKrGd1m8Y0HOwoUykyWSGL',
                  consumer_secret='MGDbvf1V5omaGVaMmwHjsaLtJlZa00RAIaqIDNVzvpi8P8ABHZ'
                  ,access_token_key='960695969745637376-DKWpgTwAWuxwAtGyRtE9SS64vyBYN0m'
                  ,access_token_secret='xkeWTdWgsGSPym3RwacumpLununkggaZ5Zl2fa1OdbNQB')
    

def Create_Update_Database():
    
    global api


    conn = sqlite3.connect('twitter.db')
    conn.execute(''' CREATE TABLE IF NOT EXISTS TWEETS(
                                    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    TWEETID varchar(30) ,
                                    USERNAME varchar(30),
                                    POSTED INTEGER DEFAULT 0);''')
    
    friends = api.GetFriends()

    for friend in friends:
    
        timeline = api.GetUserTimeline(user_id=friend.id, count=COUNT)
        for t in timeline:

            conn.execute('''INSERT INTO TWEETS (TWEETID, USERNAME)
                                      VALUES (?,?);''', (t.id_str, t.user.name))

    conn.commit()
    epiloges = len(friends)*COUNT        
    conn.close()

def Retweet(posted):
    
    global api, deleted
    funny=False
    
    while (funny==False):    
        
        
        #Sundesh sth bash
        conn = sqlite3.connect('twitter.db')
        
        #Count gia posa tweets periexei h bash
        cur = conn.execute("SELECT COUNT(ID) FROM TWEETS;")
        for r in cur:
            epiloges = [r[0]]
        
        floatTweet = random.random()*epiloges[0]
        theTweet = int(floatTweet)
        cur = conn.execute("SELECT TWEETID, POSTED FROM TWEETS WHERE ID=?;", (theTweet,))
        
        for r in cur:
            intID = [r[0], r[1]]

        
        if (not(intID[1])):
            status = api.GetStatus(intID[0])
            if (not(status.urls)):
                if(not(status.in_reply_to_screen_name)):
                    if(not(status.user_mentions)):
                        funny = True

    #print status    
    try:
        posted = True
        api.PostRetweet(status_id=intID[0])
        cur = conn.execute("UPDATE TWEETS SET POSTED=1 WHERE ID=?;", (theTweet,))
        #print intID
    except Exception as error:
        print "Exception caught"
        print str(error)
        posted = False
        cur = conn.execute("UPDATE TWEETS SET POSTED=1 WHERE ID=?;", (theTweet,))

    finally:
        conn.close()
    return posted
    


#------------------------------------MAIN----------------------------------------------#

def main():
    
    start = time.clock()
    SLEEP_TIME = 18 #seconds
    BOT_O_CLOCK = 18 #seconds

    print "Now starting Humor_bot_v0.01\n"
    Login()

    #api.UpdateProfile(description="No original content, i am bot 🤖  🤖  🤖 Bot is: ON")

    print "Login successfull! Bot is: ON"
    while(True):

        print "Creating or updating Database"
        print "..."
        Create_Update_Database()
        
    
        while(True):
            posted = False
            while (posted == False):
                posted = Retweet(posted)
            print "I just retweeted! Check it here: 'https://twitter.com/G_Tasop'"
            print "Time now:", strftime("%d %b %H:%M:%S", localtime())
            print "Next retweet in", SLEEP_TIME, "seconds"
            print "..."
            time.sleep(SLEEP_TIME)
            if ( (time.clock() - start) > BOT_O_CLOCK):
                break
        if ( (time.clock() - start) > BOT_O_CLOCK):
            break

    api.UpdateProfile(description="No original content, i am bot 🤖  🤖  🤖 Bot is: OFF")
    
    api.ClearCredentials()

    print "Humor_bot_v0.01 has terminated"


if __name__ == "__main__":
    main()
