import csv
import tweepy as tw

my_api_key = 'cpyIWxZyCUWJUb8g9YgHZVcKr'
my_api_secret = 'nj0D1ppgutppIpftZZkDTcD4Dq8eOUFGWRN3iVu8EuGTHRSNm1'

auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)

fp_data = api.get_user('sds')

search_query = "#covid19 -filter:retweets"

tweets = tw.Cursor(api.search_tweets,
              q=search_query,
              lang="en",
              until="2022-10-28").items(50)

with open('test.csv', 'w', encoding='UTF-8') as f:
    writer = csv.writer(f)

    for tweet in tweets:
        writer.writerow([tweet.created_at, tweet.text.encode('utf-8')])
        print(tweet.created_at, tweet.text.encode('utf-8'))
    
