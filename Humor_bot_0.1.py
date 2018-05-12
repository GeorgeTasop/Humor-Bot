import twitter
import sqlite3
import time
from time import strftime, localtime
import random
import sys

api = 0
COUNT = 50

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
    conn.close()

def Retweet():
    global api

    funny=False
    posted = False

    #Sundesh sth bash
    conn = sqlite3.connect('twitter.db')
    
    #Count gia posa tweets periexei h bash
    cur = conn.execute("SELECT COUNT(ID) FROM TWEETS;")
    for r in cur:
        epiloges = [r[0]]

    
    while (funny==False or posted == False):
        
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

    
        if (funny == True):
            try:
                api.PostRetweet(status_id=intID[0])
                conn.execute("UPDATE TWEETS SET POSTED=1 WHERE ID=?;", (theTweet,))
                posted = True
                print "Mphka sto try"
            except Exception as error:
                print "Exception caught"
                print "ERROR: " + str(error)
                posted = False
                conn.execute("UPDATE TWEETS SET POSTED=1 WHERE ID=?;", (theTweet,))

    conn.commit()
    conn.close()
    


#------------------------------------MAIN----------------------------------------------#

def main():
    
    SLEEP_TIME = 10 #seconds
    BOT_O_CLOCK = 30 #seconds

    print "Now starting Humor_bot_v0.2...\n"
    print "Loging in to Twitter account..."
    Login()

    #api.UpdateProfile(description="No original content, i am bot 🤖  🤖  🤖 Bot is: ON")

    print "Login successfull! Bot is: ON\n"
    

    print "Creating Database..."
    Create_Update_Database()
    print "Database created!\n"
    
    start = time.clock()
    
    while(True):
        print "Starting Retweet function..."
        Retweet()
        print "I just retweeted! Check it here: 'https://twitter.com/G_Tasop'"
        print "Time now:", strftime("%d %b %H:%M:%S", localtime())
        print "Next retweet in", SLEEP_TIME, "seconds\n"
        print "...\n"
        time.sleep(SLEEP_TIME)
        if ( (time.clock() - start) > BOT_O_CLOCK):
            break
        

    #api.UpdateProfile(description="No original content, i am bot 🤖  🤖  🤖 Bot is: OFF")
    
    api.ClearCredentials()

    print "Humor_bot_v0.01 has terminated"


if __name__ == "__main__":
    main()
