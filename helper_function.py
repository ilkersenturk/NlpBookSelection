def cleanText(rawtext):
    import re
    # lower / upper case
    text = rawtext.lower()
    
    #removing uni characters
    text_encode = text.encode("ascii", "ignore")
    text = text_encode.decode()

    # \t\n\
    text = re.sub(r'[\t|\n]+','',text)
    #removing 0903hello any word mixof 
    text = re.sub(r'[0-9]+[A-Za-z]+','',text)
    text = re.sub(r'[A-Za-z]+[0-9]+','',text)
    
    #punctuations
    text = re.sub(r"[^\w\s]+","",text)
    return text
    
    
def removeStopWords(text, unwanted):
    import nltk
    from nltk.corpus import stopwords
    
    stop_words = stopwords.words("english")
    stop_words.extend(unwanted)
    
    return " ".join([word for word in nltk.word_tokenize(text) if word not in stop_words])
    
def stemText(text):
    import nltk
    from nltk.stem import PorterStemmer
    stemmer = PorterStemmer()
    
    return " ".join(stemmer.stem(word) for word in nltk.word_tokenize(text))



def word_pos_tagger(word):
    import nltk
    from nltk.corpus import wordnet
    tag = nltk.pos_tag([word])[0][1][0]
    
    
    wordnet_map = {
        "N": wordnet.NOUN,
        "V": wordnet.VERB,
        "J": wordnet.ADJ,
        "R": wordnet.ADV
        }
    return wordnet_map.get(tag, wordnet.NOUN)


def lemmaText(text):
    
    import nltk 
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
   
    return " ".join([lemmatizer.lemmatize(word, word_pos_tagger(word)) for word in nltk.word_tokenize(text)])