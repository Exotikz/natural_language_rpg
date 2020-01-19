import nltk
from nltk.corpus import stopwords

# French
french_stopwords = set(nltk.corpus.stopwords.words('french'))

def term_frequency(text):
    words = nltk.word_tokenize(text)
    # remove single char and punctuation
    words = [word for word in words if len(word) > 1]
    # remove numbers
    words = [word for word in words if not word.isnumeric()]
    # lower
    words = [word.lower() for word in words]
    # remove stop words
    words = [word for word in words if word not in french_stopwords]

    # frequency
    return nltk.FreqDist(words)