import re
import string
from bs4 import BeautifulSoup





corpus=[
    "Hello, there I am am a student from metropolia university of applied science",
    "I study computer science and I love to build stuff",
    "I love coding and my favourite languages are C,C++ and python, I also love building embedded devices"
]


def clean_text(text):
    text=text.lower() #makes lowercase
    text=re.sub(r'\d+', '', text) #remove numbers
    text=text.translate(str.maketrans('', '', string.punctuation)) #remove punctuation
    text=re.sub(r'\W', '', text) #remove special characters
    text=BeautifulSoup(text, "html.parser").get_textU()
    return text

cleaned_corpus= [clean_text(doc) for doc in corpus ]
print(cleaned_corpus)
