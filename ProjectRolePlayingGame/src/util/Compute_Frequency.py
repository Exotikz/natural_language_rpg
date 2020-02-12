import nltk
from nltk.corpus import stopwords

# Français
french_stopwords = set(nltk.corpus.stopwords.words('french'))

def raw_text(text):
    words = nltk.word_tokenize(text)
    # enlève les lettres seules et la ponctuations
    words = [word for word in words if len(word) > 1]
    # lower case
    words = [word.lower() for word in words]
    # enlève les "stop words"
    return [word for word in words if word not in french_stopwords]

def term_frequency(text):
    # fréquence
    return nltk.FreqDist(raw_text(text))