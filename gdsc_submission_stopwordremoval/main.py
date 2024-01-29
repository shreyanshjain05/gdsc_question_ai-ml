import nltk
from nltk.corpus import stopwords

# Sample words (replace it with your actual list of words)
text ='''Welcome to the world of Natural Language Processing (NLP)! In this vast landscape, we explore the power of language.
Text pre-processing is crucial to lowercasing, tokenization, and removing special characters.
Stopword removal and stemming help reduce the dimensionality of the data enhancing analysis efficiency. Handling contractions ensures consistent representation, and spell-checking corrects any inadvertent errors.
Abbreviations, such as "USA", can be expanded to maintain clarity and consistency in the text.
URLs, like https://example.com, are often replaced with generic labels like [URL] during pre-processing.
Imagine a world where every piece of text is perfectly cleaned and ready for advanced NLP tasks.
Sentiment analysis, named entity recognition, and machine translation all benefit from robust text pre-processing.
Each line in this extended paragraph poses a unique challenge for pre-processing algorithms to tackle.
The task becomes more complex when dealing with diverse languages, slangs, and domain-specific terms.
However, with careful handling of HTML tags, code snippets, and various noise removal techniques, we pave the way for accurate analyses.
Natural Language Processing is a field that constantly evolves, demanding adaptability in pre-processing strategies.
Handling numbers, such as 123 and 4.56, requires careful consideration of their impact on downstream tasks.
A well-pre-processed text is like a canvas ready for the artist - in this case, the NLP model - to paint insights.
Imagine the power of sentiment analysis on a massive scale, deciphering emotions from social media posts in real-time.
The challenges may seem daunting, but the rewards are immense - a deeper understanding of human communication.
Now, let's jump deeper into the intricacies of text pre-processing and its role in the broader NLP ecosystem.'''


# Getting English stop words
stop_words = set(stopwords.words('english'))

# Removing stopwords


# Stopwords are removed in NLP to focus on the more meaningful and informative words in a text. This is often done to reduce noise, improve efficiency in processing, and highlight keywords that carry the essential meaning of the text

# Getting "English" stop words
filtered_text = [word for word in text if word.lower() not in stop_words]

# Printing the results
print("Original words:", text)
print("After stop word removal:", filtered_text)
