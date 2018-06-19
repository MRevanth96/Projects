from textblob import TextBlob
import sys, tweepy
import matplotlib.pyplot as plt

def percentage(part,whole):
    return (100 * (float(part)/float(whole)))

consumerKey = "czUEK7CQtOLW5G8UquteAZbCV"
consumerSecret = "0ogkcEBJ5tzOCcWiQbfbVOty0zZtXCSt0gJBf96YvbpGegVNwI"
accessToken = "1509784184-mtSkV8QjKWgfDuvRKvgDaaF2KC0J28h2skRLmtf"
accessTokenSecret = "T6T5wIEllMmLRS95muPGxL5HFyOtgW8LPJB8PII8RcRUG"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

searchTerm = input ("Enter Keyword/hashtag to search about : ")
noOfSearchterms = int(input("Enter how many tweets to analyse : "))

tweets = tweepy.Cursor(api.search, q=searchTerm).items(noOfSearchterms)

positive = 0
negative = 0
neutral = 0
polarity = 0


for tweet in tweets:
    analysis = TextBlob(tweet.text)
    polarity +=analysis.sentiment.polarity

    if(analysis.sentiment.polarity==0):
        neutral += 1
    elif(analysis.sentiment.polarity < 0.00):
        negative += 1
    elif(analysis.sentiment.polarity > 0.00):
        positive += 1
        
positive = percentage (positive, noOfSearchterms)
negative = percentage (negative, noOfSearchterms)
neutral = percentage (neutral, noOfSearchterms)
polarity = percentage (polarity, noOfSearchterms)

positive = format(positive, '.2f')
negative = format(negative, '.2f')
neutral = format(neutral, '.2f')

print ("How peoples are reacting on " + searchTerm + " by analysing " + str(noOfSearchterms) + " Tweets. " )

if (polarity == 0):
    print ("Neutral")
if (polarity < 0.00):
    print ("Negative")
if (polarity > 0.00):
    print ("Positive")

labels = ['Positive ['+str(positive) + ' %]', 'Negative ['+str(negative) + ' %]', 'Neutral ['+str(neutral) + ' %]']
sizes = [positive, negative, neutral]
colors = ['yellowgreen' , 'gold', 'red' ]
patches, texts =plt.pie(sizes, colors=colors, startangle =90)
plt.legend(patches,labels, loc = "best")
plt.title("How peoples are reacting on " + searchTerm + " by analysing " + str(noOfSearchterms) + " Tweets. ")
plt.axis('equal')
plt.tight_layout()
plt.show()
