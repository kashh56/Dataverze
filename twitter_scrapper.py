import tweepy
import pandas as pd
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch API credentials from .env
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")  # For v2 API

def authenticate_twitter():
    """Authenticate with Twitter API"""
    client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)
    return client

def fetch_tweets(keyword, max_tweets=100):
    """Fetch tweets related to a specific keyword."""
    client = authenticate_twitter()
    tweets = client.search_recent_tweets(query=keyword, tweet_fields=["created_at", "text", "lang"], max_results=max_tweets)

    tweet_list = []
    for tweet in tweets.data:
        if tweet.lang == "en":  # Filter only English tweets
            tweet_list.append({"Date": tweet.created_at, "Tweet": tweet.text})

    df = pd.DataFrame(tweet_list)
    return df
