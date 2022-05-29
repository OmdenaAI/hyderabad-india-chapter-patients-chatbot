# Task 3: NLP Sentiment Analysis

## RELEVANCE OF THE TASK
1. Sentiment Analysis is the process of determining the emotional tone behind a series of words, used to gain an understanding of the attitudes, opinions, and emotions expressed within an online mention.
2. Here, in our project, we tried to classify the tweets based on the patient's experience with the overall process during the treatment, such as how did they feel while the treatment, were they scared, nervous, or pretty calm, was the hospital staff helpful, etc
3. VADER was an excellent way to handle this problem because our data was unlabeled for sentiments. Additionally, the fact that it also deals with preprocessing, acronyms, and emoticons, which may give more insight into properly classifying the data, was a plus.
4. VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media.
5. It uses a combination of A sentiment lexicon is a list of lexical features (e.g., words) which are generally labeled according to their semantic orientation as either positive, negative, or neutral. It not only tells about the sentiment score but also tells us about how positive, negative, or neutral a sentiment is.

## STEPS PERFORMED:

### 1. ACTIVE LEARNING FOR LABELLING THE DATA AS “RELEVANT” OR “IRRELEVANT”
* Manual Annotation of 1.4k tweets
* Use of Active learning for text classification into relevant (patient experience) & irrelevant tweets
* Libraries: Small-text using Transformer as a classifier
* HuggingFace 

### 2. FILTERING THE DATA TO MAKE THE CORPUS CUSTOMIZED TO THE PROJECT IDEA
* The following was the distribution of tweets in the corpus of 62273 tweets
  * Relevant - 23001
  * Irrelevant – 39272
* The irrelevant tweets were those containing any ads/promotions, government schemes or fund raisers, which were later dropped.

### 3. PERFORM SENTIMENT ANALYSIS FOR 3 SENTIMENTS USING VADER
* We used VADER to perform Sentiment Analysis.
* The data was classified into 3 sentiments namely:
  * Positive
  * Negative
  * Neutral 


