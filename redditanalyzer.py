import praw
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

reddit = praw.Reddit(
    client_id= 'yj6jZT741zUiN1Dq_OHRaw',
    client_secret='x8BcJSqVaGk7yt9RBzdTxsSh0BHkUg',
    user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0',
)

analyzer = SentimentIntensityAnalyzer()

def categorize_sentiment(comment):
    
    
    sentiment_score = analyzer.polarity_scores(comment)
    
   
    if sentiment_score['compound'] >= 0.05:
        return 'Positive'
    elif sentiment_score['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def fetch_comments(post_url):
   
    submission = reddit.submission(url=post_url)
    submission.comments.replace_more(limit=None)  
    
   
    categorized_comments = {'Positive': [], 'Negative': [], 'Neutral': []}
    for comment in submission.comments.list():
        sentiment = categorize_sentiment(comment.body)
        categorized_comments[sentiment].append(comment.body)
    
    return categorized_comments


if __name__ == "__main__":
    post_url = 'https://www.reddit.com/r/MalayalamMovies/comments/1bf591o/anchakkallakokkan_അഞചകകളളകകകൻ_reviews_and_ratings/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button'
    comments = fetch_comments(post_url)
    
    print("Number of Positive Comments:", len(comments['Positive']))
    print("Number of Negative Comments:", len(comments['Negative']))
    print("Number of Neutral Comments:", len(comments['Neutral']))