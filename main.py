import tweepy
consumer_key='gdDxloJGzQvSbx22I3vsRqbHL'
consumer_secret='oPjxW9OZX09PFoik0rs8wy4OatPqppsbutENy9xw0QVULjhpNE'
access_token='1167602298517778432-LQie0aNho3EDHgBGrWBBKBnpkEnOyc'
acces_token_secret='C7OwRh6LJkG4fW0Pe67IZ586BDdYASy8o7DY3uDFEgHC9'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,acces_token_secret)
api = tweepy.API(auth)
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during Authentication")

"""tweet = "Aishwarya Rai"
photo= 'C:\\Users\\Himanshu Sharma\\Downloads\\photo.png'
status = api.update_with_media(photo,tweet)
api.update_status(status=tweet)"""

user = api.get_user('ArvindKejriwal')
print("user details:")
print(user.name)
print(user.description)
print(user.location)
print("Last 20 Followers:")
for follower in user.followers():
    print(follower.name)
