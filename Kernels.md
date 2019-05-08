# Exam Project: The formation of ISIS' Social Media Network

Group members: Zeyu Zhao, Helge Zille, Edith Zink, Sina Smid

## Previous Kernels on Kaggle (selection)

### Isis Tweet Network Analysis - Georgi D. Gospodinov
[Kaggle Kernel](https://www.kaggle.com/ggospodinov/tweet-analysis2)

- intersection between tweets -> weight of link between two users
- aggregated pairwise co-occurence of character strings in tweet for each username combination, normalized by the sum of all tweets from both usernames.
- Each connection between usernames indicates an aggregated number of shared words between usernames using pairwise tweet-to-tweet comparisons, normalized by the number of tweet and filtered to ignore strings of length $<$3.
- generates an undirected, weighted graph.
- apply filtration
- can we just assume common language and translate non-english tweets?
- it would be very important to delete "irrelevant" words for this approach.

What do they look at in the network?
- Unweighted/weighted degree distribution.
- Closeness centrality distribution.
- Eigenvector centrality distribution.
- Clustering coefficient distribution.
- Edge weight distribution.
- Betweenness and edge-betweenness centrality.
- Closeness centrality distribution.
- Network visualization with node colors according to closeness centrality, eigenvector centrality, ...
- Community structures, clusters (different approaches).
- Diameter of the network.
- Global clustering coefficient.
- Minimum weight spanning tree.
- Path length distribution.

### Exploring ISIS(?) Tweets - Violinbeats
[Kaggle Kernel](https://www.kaggle.com/violinbeats/notebook-0427671092ae887aa87e/code)

R script which does mostly descriptive analysis.
There are some things we might want to include into our report as well:
- Distribution of the number of tweets each user posted within period of observation
- Check unique name and username pairs -> generate ID variable
- Distribution number of followers
- Distribution number of statuses
- Timeline with number of tweets per month/ per hour of the day
- Identify top words
- Create word-cloud with words that appeared at least 100 times

### Analysing "How ISIS Uses Twitter" using social network cluster analysis - HuwFulcher
[Kaggle Kernel](https://www.kaggle.com/huwfulcher/social-cluster-analysis?fbclid=IwAR1MQX34OUV-QJV6-GAkB2aajKqf2JJ2v6xpJvBIut13qz6iVq5co_fOOKo)
- How many users in the dataset tweet each other?
- Code copied into descriptive analysis
- TO DO: Make network look nice!

### Text Analysis Using the Tweets - AdhokshajaPradeep
[Kaggle Kernel](https://www.kaggle.com/adhok93/text-analysis-using-the-tweets)
- identify most frequently occurring terms in Tweets (removing non-english words)
- Find words/terms associated with the most frequent terms
- cluster words (hierarchical clustering)
- network of terms to show relationship between frequent terms

### Current Events and ISIS in Twitter - Omar Pena
[Kaggle Kernel](https://www.kaggle.com/greyfaux/quick-look)

- Code also copied into the descriptive analysis.

### Drawing Network for Pro-ISIS Tweets - Jason Liu
[Kaggle Kernel](https://www.kaggle.com/jiashenliu/drawing-network-for-pro-isis-tweets)
- Python Script :) meaning that I was able to include it into our code.
- approach should lead to similar results as the one of HuwFulcher, but doesn't. Maybe look into the code again.
