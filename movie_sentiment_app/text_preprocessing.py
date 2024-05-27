import numpy as np
import pandas as pd
import nltk
import re
import string
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
import pickle



# remove Punctuations
def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


# remove Html Tags
def remove_html(text):
    pattern = re.compile(r'<.*?>')
    return pattern.sub('', text)


# Convert numbers into words
# import the inflect library
import inflect
p = inflect.engine()

# convert number into words
def convert_number(text):
    # split string into list of words
    temp_str = text.split()
    # initialise empty list
    new_string = []

    for word in temp_str:
        # if word is a digit, convert the digit
        # to numbers and append into the new_string list
        if word.isdigit():
            temp = p.number_to_words(word)
            new_string.append(temp)

        # append the word as it is
        else:
            new_string.append(word)

    # join the words of new_string to form a string
    temp_str = ' '.join(new_string)
    return temp_str


# remove whitespace from text
def remove_whitespace(text):
    return  " ".join(text.split())


# removing stopwords and word tokenizing and stemming
def remove_stopwords(text):
    stop_words = set(stopwords.words("english"))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    stems = [stemmer.stem(word) for word in filtered_text]
    return stems


# converting list into string
def prepro(text_list):
  return " ".join(text_list)

def text_preprocessing(text):
    text = text.lower()
    text = remove_html(text)
    text = convert_number(text)
    text = remove_whitespace




