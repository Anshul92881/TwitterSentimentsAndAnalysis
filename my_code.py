from textblob import TextBlob
import sys,tweepy
import matplotlib.pyplot as plt


def percentage(part, whole):
    return 100 * float(part)/float(whole)


consumerKey = '5vU8aeRu8FxEm72kcgPHkDtgN'
consumerSecret = '0ghRz5vYnl4ZwTTKDExRFy9GXO8RrDjvJpmN6Ujs2kFyi9zTNR'
accessToken = '1296862539150692357-yiBfH4tUav1xdnqx9eXEXRlh86ezmP'
accessTokenSecret = 'bgo3FJz4flOpZ2y65EciWEMO7oJswC3b9Tsk8e8nc60RU'

auth = tweepy.OAuthHandler(consumerKey,consumerSecret)
auth.set_access_token(accessToken , accessTokenSecret)
api = tweepy.API(auth)

searchTerm = input("Enter the Keyword or the Hashtag to search about: ")
noOfSearchTerms = int(input("Enter the number of tweets to analyze: "))


tweets = tweepy.Cursor(api.search_tweets, q=searchTerm).items(noOfSearchTerms)


positive = 0
negative = 0
neutral = 0
polarity = 0

#Checking the Polarities
for tweet in tweets:
    analysis = TextBlob(tweet.text)
    polarity += analysis.sentiment.polarity

    if (analysis.sentiment.polarity == 0):
        neutral += 1
    if (analysis.sentiment.polarity > 0.00):
        positive += 1
    if (analysis.sentiment.polarity < 0.00):
        negative += 1

# calculating the percentages
positive = percentage(positive, noOfSearchTerms)
negative = percentage(negative, noOfSearchTerms)
neutral = percentage(neutral, noOfSearchTerms)
polarity = percentage(polarity, noOfSearchTerms)

# percentages only upto two decimal places
positive = format(positive, '.2f')
neutral = format(neutral, '.2f')
negative = format(negative, '.2f')


print("How people are reacting on " + searchTerm + " by analyzing " + str(noOfSearchTerms) + " tweets.")


if(polarity == 0):
    print("Neutral")
elif(polarity < 0.00):
    print("Negative")
elif(polarity > 0.00):
    print("Positive")


labels = ['Positive['+str(positive)+'%]', 'Neutral['+str(neutral)+'%]', 'Negative['+str(negative)+'%]']
sizes = [positive, neutral, negative]
colors = ['yellow', 'green', 'red']
patches , texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title('How people are reacting on ' + searchTerm + ' by analyzing ' + str(noOfSearchTerms) + ' Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()