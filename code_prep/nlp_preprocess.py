import re
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import unidecode
import contractions
from textblob import Word
import inflect
import spacy
from nltk.stem import WordNetLemmatizer
nlp = spacy.load('en_core_web_md')
stopwords=stopwords.words('english')

### Removing Punctuations
def remove_punct(sentence):
    return re.sub(r'[^\w\s]','', sentence)

### Extracting the root words (lemmatization?) - might take long time to run
def root_words(sentence):
    doc = nlp(sentence)
    lemm_sent = []
    for token in doc:
        lemm_sent.append(token.lemma_)
    return ' '.join(lemm_sent)

### Removing Accents - might take long time to run
def remove_accents(sentence):
    return unidecode.unidecode(sentence)

### Converting to Lower case
def to_lower(sentence):
    return sentence.lower()

### Removing Stop words
def remove_stopwords(sentence, stopwords=stopwords):
    return " ".join([word for word in sentence.split() if word not in stopwords])

### Removing Extra Spaces
def remove_spaces(sentence):
    return re.sub('\s{2,}', ' ', sentence).strip()

### Clean typos - might take long time to run
def clean_typos(sentence):
    correct_sent = ''
    for word in sentence.split():
        correct_sent += Word(word).correct() + ' '
    return correct_sent.strip()

### number handling (1 -> one) - might take long time to run
def number_translate(sentence):
    p = inflect.engine()
    sent_split = sentence.split()
    for i, word in enumerate(sent_split):
        if word.isdigit() and int(word) < 101:
            sent_split[i] = p.number_to_words(word)
    return ' '.join(sent_split)

### Expand Contractions (don't -> do not) - might take long time to run
def expand_contractions(sentence):
    return contractions.fix(sentence)

### Tokenziation
def tokenize(sentence):
    return word_tokenize(sentence)

def standard_preprocess(sentence, stopword=stopwords):
    sentence = remove_punct(sentence)
    sentence = to_lower(sentence)
    sentence = remove_stopwords(sentence, stopword)
    sentence = remove_spaces(sentence)
    return sentence
