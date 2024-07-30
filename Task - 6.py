#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from textblob import TextBlob

# Load data
file_path = r"C:\Users\Admin\Downloads\disney_plus_titles.csv"
df = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(df.head())


# ## 1. Time Series Analysis

# In[2]:


# Analyzing the release trends over the years
df['release_year'] = pd.to_datetime(df['release_year'], format='%Y')
release_year_counts = df['release_year'].dt.year.value_counts().sort_index()

# Plotting the release trends
plt.figure(figsize=(12, 6))
plt.plot(release_year_counts.index, release_year_counts.values, marker='o')
plt.title('Number of Releases per Year')
plt.xlabel('Year')
plt.ylabel('Number of Releases')
plt.grid(True)
plt.show()

# Decompose time series data (if applicable)
decomposed = seasonal_decompose(release_year_counts, model='additive', period=1)
decomposed.plot()
plt.show()


# ## 2. Sentiment Analysis on Descriptions

# In[3]:


def get_sentiment(description):
    analysis = TextBlob(description)
    return analysis.sentiment.polarity

df['sentiment'] = df['description'].apply(get_sentiment)

# Display sentiment analysis results
print(df[['title', 'sentiment']].head())

# Plot sentiment distribution
plt.figure(figsize=(12, 6))
plt.hist(df['sentiment'], bins=20, color='skyblue', edgecolor='black')
plt.title('Sentiment Polarity Distribution')
plt.xlabel('Sentiment Polarity')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# ## 3. Clustering using KMeans on descriptions (text data)

# In[5]:


# Convert text data to TF-IDF features
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['description'].dropna())

# Perform KMeans clustering
num_clusters = 5
kmeans = KMeans(n_clusters=num_clusters, n_init=10, random_state=42)
kmeans.fit(tfidf_matrix)

# Add cluster labels to the original dataframe
df['cluster'] = kmeans.labels_

# Display clustering results
print(df[['title', 'cluster']].head())

# Plot the number of titles in each cluster
plt.figure(figsize=(12, 6))
df['cluster'].value_counts().sort_index().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Number of Titles per Cluster')
plt.xlabel('Cluster')
plt.ylabel('Number of Titles')
plt.grid(True)
plt.show()

