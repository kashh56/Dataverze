
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(df, column="Online_Reviews"):
    """Perform sentiment analysis on text data (Reviews, Tweets, etc.)."""
    df["Sentiment_Score"] = df[column].apply(lambda x: sia.polarity_scores(str(x))["compound"])
    
    # Classify Sentiments
    df["Online_Sentiment"] = df["Sentiment_Score"].apply(lambda x: "Positive" if x > 0.05 else "Negative" if x < -0.05 else "Neutral")
    return df
