import pandas as pd
import re
import nltk
import string
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import words
from nltk.corpus import wordnet
from nltk.corpus import stopwords
import unidecode
import contractions
from textblob import Word
import inflect
import spacy
nlp = spacy.load('en_core_web_md')

### Removing Punctuations
def remove_punct(sentence):
    return re.sub(r'[^\w\s]','', sentence)

### Extracting the root words (lemmatization?)
def root_words(sentence):
    doc = nlp(sentence)
    lemm_sent = []
    for token in doc:
        lemm_sent.append(token.lemma_)
    return ' '.join(lemm_sent)

### Removing Accents
def remove_accents(sentence):
    return unidecode.unidecode(sentence)

### Converting to Lower case
def to_lower(sentence):
    return sentence.lower()

### Removing Stop words
def remove_stopwords(sentence, stopwords):
    return " ".join([word for word in sentence.split() if word not in stopwords])

### Removing Extra Spaces
def remove_spaces(sentence):
    return re.sub('\s{2,}', ' ', sentence).strip()

### Clean typos
def clean_typos(sentence):
    correct_sent = ''
    for word in sentence.split():
        correct_sent += Word(word).correct() + ' '
    return correct_sent.strip()

### number handling (1 -> one)
def number_translate(sentence):
    p = inflect.engine()
    sent_split = sentence.split()
    for i, word in enumerate(sent_split):
        if word.isdigit() and int(word) < 101:
            sent_split[i] = p.number_to_words(word)
    return ' '.join(sent_split)

### Expand Contractions (don't -> do not)
def expand_contractions(sentence):
    return contractions.fix(sentence)

### Tokenziation
def tokenize(sentence):
    return word_tokenize(sentence)

punct_test = "Hello, I am Zach! Nice to meet you. Hello? ~"
accent_test = "orčpžsíáýd"
space_test = "   i  am zach.  xiong  ha     "
typo_test = 'appple bannana heello'
contractions_text = "I'm Zach. I've been study chinese for 1022 year. I'll go to US for my degree."
lemma_test = 'I joined WSP 2.5 years ago as a graduate engineer.'
# print(remove_accents(accent_test), 'finished!!!')
punct_test = remove_punct(accent_test)
# print(remove_stopwords(punct_test, ['you']))
# print(root_words(lemma_test))
print(punct_test)
