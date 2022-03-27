import nltk
import requests
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import docx2txt

def Degree(text):
  text = text.lower()
  a = []
  if ('bachelor' in text) or ('bs' in text) or ('undergraduate' in text) or ('b.s in text'):
    a.append('Bachelor')
  elif 'Master'.lower() in text or ('MS'.lower() in text):
    a.append('Master')
  elif 'graduate' in text:
    a.append('Graduate Level')
  elif 'phd' in text:
    a.append('phd')
  else:
    pass
  return a

def Sponsor(text):
   key = ['work visas','work visa','U.S.','U.S.Citizen','Permanent Residence']
   for i in key:
     if i in text:
       return True
     else:
       return False

def Tools(text):
    Tlist = []
 

    # function to test if something is a noun
    is_noun = lambda pos: pos[:2] == 'NN'
    # do the nlp stuff
    tokenized = nltk.word_tokenize(text)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
  

    Tlist = []
    tools = ['Python', 'C','R', 'C++','java', 'hadoop','scala','flask','pandas','spark','scikit-learn',
                      'numpy','php','SQL','MySQL','css','mongdb','nltk','fastai' , 'keras', 'pytorch','tensorflow',
                    'linux','Ruby','JavaScript','django','reactjs','ai','ui','tableau', 'aws', 'node.js', 
                      'hive', 'nodejs', 'git','Microsoft','MS Office','Excel','Google Analytics']
    
    n = 0
    for i in tools:
      i = i.lower()
      for j in nouns:
        j = j.lower()
        if i == j:
          Tlist.append(tools[n])
      n +=1
    return list(set(Tlist))

def SkillSet(text):
    text = text.lower().split('\n')
    Mlist = []
    A = ['Machine Learning','ML','Programming','Software Development','Data Pipelines']
    n = 0
    for i in A:
      i = i.lower()
      for j in text:
        if i in j:
           Mlist.append(A[n])
      n +=1
    return list(set(Mlist))



def Keyword(text):
    delim = ","
    Tool = Tools(text)
    T=''
    for i in Tool:
      T = T+str(i)+delim
    Skills = SkillSet(text)
    Sk = '' 
    for i in Skills:
      Sk = Sk + str(i) + delim
    
    
    
    Degrees = Degree(text)
    D = ''
    for i in Degrees:
      D = D + str(i) + delim
    S = Sponsor(text)
    return D,T,Sk,S