import tweepy
import time

consumer_key = 'x1jyiPxfzNO9KDg9CovD3VGWU'
consumer_secret = 'AztttzbGZC0EPLZeu6JvU205Vhf0mpAG2mXd09EI6NaXBkRdA9'
access_token = '1787284900401610752-APbP7aTGE8twNEj1kVM2b9utDdIfZg'
access_token_secret = 'SAnXDKYv0444kFftqnJsXTNYYANWlX74ZdkJZ3Y2vEVJE'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAJXzuQEAAAAAGH150dvDUhaboiX3PK40X0pcHeU%3D1xZKE7CHHuTdjGp5EkJVbzmAZSZmeBWLnkPiTNwqOc8twbXrN8'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret, wait_on_rate_limit=True)

def reply_to_tweets():
    print('Bot is running and looking for tweets...')
    last_mention_id = None
    while True:
        try:
            # Mencari tweet yang menyebut akun Anda menggunakan API v2
            if last_mention_id:
                mentions = client.get_users_mentions(client.get_me().data.id, since_id=last_mention_id)
            else:
                mentions = client.get_users_mentions(client.get_me().data.id)

            if mentions.data:
                for mention in mentions.data:
                    last_mention_id = mention.id
                    print(f"Tweet by {mention.author_id} - {mention.text}")
                    if not mention.referenced_tweets:
                        # Balas tweet
                        client.create_tweet(in_reply_to_tweet_id=mention.id, text=f"@{mention.author_id} Terima kasih atas mention-nya!")
                        print(f"Replied to {mention.author_id}")
            time.sleep(60)  # Tunggu 1 menit sebelum memeriksa lagi
        except tweepy.TweepyException as e:
            print(f"Error: {e}")
            time.sleep(60)

# Jalankan fungsi
reply_to_tweets()



   
   
