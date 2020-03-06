from typing import List
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

# ! Absolument nécessaire de lancer au moins une fois :
# ! nltk.download()
# ! nltk.download("stopwords") 
# ! pour que la suite fonctionne.
# Français
french_stopwords = set(stopwords.words('french'))

def raw_text(text) -> List[str]:
    # Tokenize divide the text in single elements, ex: "Lorem ipsum." -> ["Lorem", "ipsum", '.']
    words: List[str] = word_tokenize(text)
    # Remove single letters and punctuation
    words = [word for word in words if len(word) > 1]
    # lower case
    words = [word.lower() for word in words]
    # Remove stop words ex: "the, of, in, a, an, etc." are stop words
    return [word for word in words if word not in french_stopwords]

def term_frequency(text):
    return FreqDist(text)

def term_frequency_without_stop_words(text):
    return FreqDist(raw_text(text))

def split_words(text):
    return word_tokenize(text, language='french')
    
def split_sentences(text):
    return sent_tokenize(text, language='french')