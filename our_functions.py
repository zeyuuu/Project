import pandas as pd
import datetime
import re
import numpy as np
import langid


def read_tweets(csv_file):
    """ Function that reads in csv file
    - csv file needs a 'time'-column with the date,time of the tweet
    - removes indication of translation from tweets and adds a dummy-column indicating translated tweets
    returns pandas Dataframe
    """

    df         = pd.read_csv(csv_file)
    df['time'] = pd.to_datetime(df.time)
    df['date'] = [datetime.datetime(x.year, x.month, x.day) for x in df.time]
    df['translated'] = [tweet.startswith('ENGLISH') for tweet in df['tweets']]
    df['tweets']     = df.tweets.apply(lambda x: re.sub(re.compile("ENGLISH TRANS[^:]*:"),'',x))

    return df


def actual_retweets(df):
    """ Function that returns two dataframes:
    1. one containing only retweets
    2. one containing only (actual) tweets

    - tweets: column with tweets

    In the orginal dataframe retweets should be marked by 'RT.'
    """
    df1 = df[df.tweets.str.startswith('RT')]

    df2 = df[df.tweets.str.startswith('RT')==0]

    return df1, df2


def mentions(df):
    """ Function that returns in-set and not-in-set mentions
    - mention follow "@" in the tweet
    - df.tweets: column containing tweets
    - df.username: column with username
    returns two np.arrays with username pairs for mentions within dataset and without.
    """
    in_set = []
    not_in_set = []
    for user, tweet in zip(df['username'], df['tweets']):
        match = re.findall(r'@\w*', tweet)

        if match != []:
            for name in match:
                if (name[1:] in df['username'].unique()) and (user != name[1:]):
                    in_set.append([user, name[1:]])
                elif user != name[1:]:
                    not_in_set.append([user, name[1:]])

    in_set = np.array(in_set)
    not_in_set = np.array(not_in_set)

    return in_set,  not_in_set


def language(df):
    """ Function that detects languages of tweets
    df.tweets: column with tweets in different languages
    returns df with new columns containing language classification and score
    """
    predictions = [langid.classify(tweet) for tweet in df['tweets']]
    df['language'], df['lg_value'] = zip(*predictions)

    return df

from nltk.stem import PorterStemmer
porter = PorterStemmer()

def stem_list(list_of_words):
    new_list = []
    for word in list_of_words:
        new_list.append(porter.stem(word))
    return new_list


import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn

def lemmatize(word_list):
    lemma_list = []
    for word in word_list:
        lemma = wn.morphy(word)
        if lemma is None:
            lemma_list.append(word)
        else:
            lemma_list.append(lemma)
    return lemma_list