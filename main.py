import discord
import tweepy

twitter_api_key = ''
twitter_api_secret = ''
twitter_bearer_token = ''
twitter_access_token = ''
twitter_access_token_secret = ''

discordToken = ''

client = discord.Client()
id = 0
screen_name = ""



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel_id = 642235926205956130
    for guild in client.guilds:
        for channel in guild.text_channels:
            print(guild.name)
            print(channel.name)
            print(channel.id)
            
    await client.get_channel(channel_id).send('https://twitter.com/' + screen_name + '/status/' + str(id) + '\n' +
                                                      'https://www.youtube.com/watch?v=V_cnK8Cd6Ag')
    await client.get_channel(channel_id).send("**It's 7pm somewhere!**")

    print("closing Discord connection")
    await client.close()



class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)
        print(status.id)
        print(status.user.screen_name)
        print('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')
        global id
        global screen_name
        id = status.id
        screen_name = status.user.screen_name
        client.run(discordToken)

    def on_error(self, status_code):
        if status_code == 420:
            print('rate limit exceeded, closing connection')
            return False
        else:
            print(status_code)
            return False

## my twitter id = 794194806
## CraigWeekend's id = 1288226864457084928
auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret)
auth.set_access_token(twitter_access_token, twitter_access_token_secret)

while True:
    api = tweepy.API(auth)
    
    print("getting data for @CraigWeekend")
    item = api.get_user("@CraigWeekend")
    print("name " + item.name)
    print("screen_name: " + item.screen_name)
    print("description: " + item.description)
    print("statuses_count: " + str(item.statuses_count))
    print("friends_count: " + str(item.friends_count))
    print("followers_count: " + str(item.followers_count))
    
    
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)
    
    print('starting stream')
    try:
        myStream.filter(follow=['1288226864457084928'])
    except:
        print('connection closed unexpectedly')
    print('stream closed')
    print('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n')



