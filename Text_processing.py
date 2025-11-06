import re
import string
from bs4 import BeautifulSoup
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt_tab')
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem import PorterStemmer, WordNetLemmatizer
import contractions
from spellchecker import SpellChecker


corpus=[
    "Hello, there I am am a student from metropolia university of applied science",
    "I study computer science and I love to build stuff",
    "I love coding and my favourite languages are C,C++ and python, I also love building embedded devices",
    "<html><body>Welcome to the website!</body></html>"
]

'''🧹 Text Cleaning
⚙️ Function: clean_text(text)
Cleans and normalizes input text by performing:

▸ Lowercasing - Converts all text to lowercase
▸ Number Removal - Strips numerical digits
▸ Punctuation Removal - Eliminates all punctuation marks
▸ Special Character Removal - Removes non-word characters
▸ HTML Tag Stripping - Extracts clean text from HTML content'''

def clean_text(text):
    text=text.lower() #makes lowercase
    text=re.sub(r'\d+', '', text) #remove numbers
    text=text.translate(str.maketrans('', '', string.punctuation)) #remove punctuation
    text=re.sub(r'\W', '', text) #remove special characters
    text=BeautifulSoup(text, "html.parser").get_text()  #remove HTML tags
    return text

cleaned_corpus= [clean_text(doc) for doc in corpus ]
print(cleaned_corpus)


'''Tokenization
Splits cleaned text into individual word tokens
Uses NLTK's word_tokenize for word-level tokenization
Requires downloading the punkt_tab tokenizer model
Processes each document in cleaned_corpus
Outputs a list of word lists (tokenized_corpus)'''

tokenized_corpus=[word_tokenize(doc) for doc in cleaned_corpus]
print(tokenized_corpus)


'''Stop Words Removal
Removes common English stop words from tokens
Uses NLTK's stopwords corpus
Filters out words like "the", "is", "and" etc.
Processes each document in tokenized_corpus
Outputs cleaned tokens in filtered_corpus'''

stop_words=set(stopwords.words('english'))
filtered_corpus = [[word for word in doc if word not in stop_words] for doc in tokenized_corpus]
print(filtered_corpus)


'''   
4. Stemming and Lemmatization
Reducing words to their base form using stemming and lemmatization.
Imports PorterStemmer and WordNetLemmatizer from NLTK.
Downloads the wordnet resource required for lemmatization.
Initializes the stemmer and lemmatizer.
Applies stemming to each word in filtered_corpus and stores the result in stemmed_corpus.
Applies lemmatization to each word in filtered_corpus and stores the result in lemmatized_corpus.
Prints both the stemmed and lemmatized versions of the corpus.'''

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

stemmed_corpus = [[stemmer.stem(word) for word in doc] for doc in filtered_corpus]
lemmatized_corpus = [[lemmatizer.lemmatize(word) for word in doc] for doc in filtered_corpus]
print(stemmed_corpus)
print(lemmatized_corpus)

'''
Contractions Handling
Expands shortened words to their full forms
Uses contractions.fix() for expansion
Processes each document in cleaned_corpus
Converts words like "can't" → "cannot", "I'm" → "I am"
Outputs expanded text in expanded_corpus
'''

expanded_corpus = [contractions.fix(doc) for doc in cleaned_corpus]
print(expanded_corpus)

'''
Converts emojis to descriptive text
Uses emoji.demojize() for conversion
Processes each document in cleaned_corpus
Transforms emojis like 😊 → :smiling_face_with_smiling_eyes:
Outputs text with emoji descriptions in emoji_corpus
'''



'''
Spell Checking
Corrects spelling errors in text
Uses pyspellchecker library
Processes each word in tokenized_corpus
Applies spell.correction() to fix misspelled words
Outputs corrected tokens in corrected_corpus
'''

spell = SpellChecker()
corrected_corpus = [[spell.correction(word) for word in doc] for doc in tokenized_corpus]
print(corrected_corpus)



'''ultimate output 
[['hello', 'student', 'metropolia', 'university', 'applied', 'science'],
 ['study', 'computer', 'science', 'love', 'build', 'stuff'],
 ['love', 'coding', 'favourite', 'languages', 'cc', 'python', 'also', 'love', 'building', 'embedded', 'devices'],''' 