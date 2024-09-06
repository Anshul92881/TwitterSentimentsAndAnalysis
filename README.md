# Twitter Sentiments and Analysis

This Python script performs sentiment analysis on tweets containing a specific keyword or hashtag using the **TextBlob** library. It fetches tweets via the **Tweepy** library, analyzes their sentiment (positive, neutral, or negative), and visualizes the results with a pie chart using **Matplotlib**.

## Key Features

- **Twitter API Integration**: Authenticates using Twitter API credentials to fetch tweets based on user input.
- **Sentiment Analysis**: Analyzes the sentiment of each tweet, categorizing them into positive, neutral, or negative.
- **Polarity Calculation**: Computes the overall polarity of the analyzed tweets to determine the general sentiment.
- **Visual Representation**: Displays a pie chart using **Matplotlib** to visually represent the sentiment distribution.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- A Twitter Developer account with API keys (consumer key, consumer secret, access token, access token secret).
- Install the required Python libraries using the following command:

```bash
pip install tweepy textblob matplotlib

Usage
To run the script, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/your-username/TwitterSentimentsAndAnalysis.git
cd TwitterSentimentsAndAnalysis
Add your Twitter API credentials in the script:

python
Copy code
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'
Run the script:

bash
Copy code
python sentiment_analysis.py
Input the search term and number of tweets to analyze:

Enter a keyword or hashtag (e.g., #Python).
Enter the number of tweets to analyze.
View the results:

The script will fetch tweets, analyze their sentiment, and display a pie chart showing the distribution of positive, neutral, and negative sentiments.
Example
When you run the script and search for a hashtag like #Python, you will see an output similar to this:

Total tweets analyzed: 100
Positive: 45%
Neutral: 35%
Negative: 20%
The sentiment distribution is also displayed in a pie chart.

Libraries Used
Tweepy: For interacting with the Twitter API.
TextBlob: For natural language processing and sentiment analysis.
Matplotlib: For plotting the sentiment data.
