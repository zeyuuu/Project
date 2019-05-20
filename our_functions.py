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
    """ Function that computes a stemmed list of words
    list_of_words: list with words to be stemmed
    returns the stemmed list
    """
    new_list = []
    for word in list_of_words:
        new_list.append(porter.stem(word))
    return new_list


import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn

def lemmatize(word_list):
    """ Function that computes a lemmatized list of words
    list_of_words: list with words to be stemmed
    returns the stemmed list
    """
    lemma_list = []
    for word in word_list:
        lemma = wn.morphy(word)
        if lemma is None:
            lemma_list.append(word)
        else:
            lemma_list.append(lemma)
    return lemma_list


def flat_list(l):
    flat_list = []
    for sublist in l:
        for item in sublist:
            flat_list.append(item)
    return flat_list


import seaborn; seaborn.set()
import matplotlib.pyplot as plt
plt.style.use('ggplot') # makes the bar charts red on grey background with grid, I think it is nice
default_red = plt.rcParams['axes.prop_cycle'].by_key()['color'][0]

period1 = [datetime.date(2015, 10, 1),datetime.date(2016, 1, 31)]
period2 = [datetime.date(2016, 2, 1),datetime.date(2016, 2, 28)]
period3 = [datetime.date(2016, 3, 1),datetime.date(2016, 4, 30)]

def plot_periods(var1, var2=None, period1=period1, period2=period2, period3=period3):
    fig, (ax1,ax2,ax3) = plt.subplots(nrows=3,ncols=1)
    ax1 = plt.subplot(311)
    ax1 = var1.plot(color=default_red, figsize=(12,8), xlim=period1, linestyle = '-')
    ax1 = var2.plot(color=default_red, figsize=(12,8), xlim=period1, linestyle = ':')

    ax2 = plt.subplot(3,1,2)
    ax2 = var1.plot(color=default_red, figsize=(12,8), xlim=period2, linestyle = '-')
    ax2 = var2.plot(color=default_red, figsize=(12,8), xlim=period2, linestyle = ':')
    
    ax3 = plt.subplot(3,1,3)
    ax3 = var1.plot(color=default_red, figsize=(12,8), xlim=period3, linestyle = '-')
    ax3 = var2.plot(color=default_red, figsize=(12,8), xlim=period3, linestyle = ':')
    plt.tight_layout()
    return fig


import gensim
from gensim.models import CoherenceModel
def compute_coherence_values(dictionary, corpus, texts, limit, start=2, step=3):
    """
    Compute c_v coherence for various number of topics

    Parameters:
    ----------
    dictionary : Gensim dictionary
    corpus : Gensim corpus
    texts : List of input texts
    limit : Max num of topics

    Returns:
    -------
    model_list : List of LDA topic models
    coherence_values : Coherence values corresponding to the LDA model with respective number of topics
    """
    coherence_values = []
    model_list = []
    for num_topics in range(start, limit, step):
        model = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, 
                                                random_state=100, update_every=1, chunksize=100, passes=10,
                                                alpha='auto', per_word_topics=True)
        model_list.append(model)
        coherencemodel = CoherenceModel(model=model, texts=texts, dictionary=dictionary, coherence='u_mass')
        coherence_values.append(coherencemodel.get_coherence())

    return model_list, coherence_values