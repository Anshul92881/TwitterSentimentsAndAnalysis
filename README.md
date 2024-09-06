## Twitter Sentiments and Analysis

This Python script performs sentiment analysis on tweets containing a specific keyword or hashtag using the TextBlob library. The script leverages Tweepy to interact with the Twitter API, allowing users to gather and analyze the sentiment of a specified number of tweets.

Key Features:
Twitter API Integration: Authenticates using Twitter API credentials to fetch tweets based on user input.
Sentiment Analysis: Analyzes the sentiment of each tweet, categorizing them into positive, neutral, or negative sentiments.
Polarity Calculation: Computes the overall polarity of the analyzed tweets, determining the general sentiment.
Visual Representation: Generates a pie chart using Matplotlib to visually represent the sentiment distribution.

Usage:
The user inputs a keyword or hashtag to search for, along with the number of tweets to analyze.
The script fetches the tweets and analyzes their sentiment (positive, neutral, negative).
A pie chart is generated to display the sentiment distribution.

Prerequisites:
Twitter Developer account and API keys (consumer key, consumer secret, access token, access token secret).
Python 3.x
Install required libraries using pip:
bash
Copy code
pip install tweepy textblob matplotlib

Libraries Used:
Tweepy: For interacting with the Twitter API.
TextBlob: For natural language processing and sentiment analysis.
Matplotlib: For plotting and visualizing the sentiment data.

How to Run:
Clone the repository.
Add your Twitter API credentials in the script.
Run the script, enter a keyword/hashtag, and specify the number of tweets to analyze.
View the sentiment analysis results in a pie chart.
