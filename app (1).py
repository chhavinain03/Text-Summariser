import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from spacy import tokens
import streamlit as st
from heapq import nlargest
import subprocess
subprocess.run("pip3 install PyPDF2".split())
subprocess.run("python3 -m spacy download en_core_web_sm".split())
import PyPDF2
from utils import (
    clean_text,
    fetch_article_text,
    preprocess_text_for_abstractive_summarization,
    read_text_from_file,
)
#---------------------Pre-Requiste------------------------#
stopwords = STOP_WORDS
punctuation = punctuation + '\n'



if __name__=="__main__":
    st.title("Text Summarizer 📝")
    st.subheader("Creator: Shreyas Dixit")
    
    n = st.sidebar.slider('Summarization %',10,90,step=10)
    n = n/100
    type=st.selectbox('Pick one', ['PDF','Text'])
    if type=="PDF":
        #Upload file
        uploaded_file = st.file_uploader("Choose a file",type=['pdf','txt','docx'])
        text = read_text_from_file(uploaded_file)
        # FileName = uploaded_file.name
        # if uploaded_file is not None:
        #     pdfFileObj = open("{FileName}", 'rb') 
        #     pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
        #     pageObj = pdfReader.getPage(0) 
        #     text = (pageObj.extractText()) 
        #     pdfFileObj.close() 
    elif type=="Text": 
        #Text
        text=st.text_area("Input text !")

    if st.button('Summarize'):
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(text)
        #Word tokenization
        tokens = [tokens.text for tokens in doc]
        word_frquency = {}
        for word in doc:
            if word.text.lower() not in stopwords:
                if word.text.lower() not in punctuation:
                    if word.text not in word_frquency.keys():
                        word_frquency[word.text] = 1
                    else:
                        word_frquency[word.text] += 1
        #Normalize the values
        max_word = max(word_frquency.values())
        for word in word_frquency.keys():
            word_frquency[word] = word_frquency[word]/max_word
        #Sentence Tokenization
        sentence_token = [sent for sent in doc.sents]
        sentence_score = {}
        for sent in sentence_token:
            for word in sent:
                if word.text.lower() in word_frquency.keys():
                    if sent not in sentence_score.keys():
                        sentence_score[sent] = word_frquency[word.text.lower()]
                    else:
                        sentence_score[sent] += word_frquency[word.text.lower()]
        #Creating a Summary
        select_length = int(len(sentence_token)*n)
        summary = nlargest(select_length,sentence_score,key = sentence_score.get)
        summary = [word.text for word in summary]
        summary = ' '.join(summary)
        st.markdown(summary)