import sys
import os
import pymysql
import nltk
import requests
import numpy as np
import pandas as pd
from pandas import json_normalize 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import docx2txt
from KeywordLocate import *

ENDPOINT="career-info.coid7kfjmyst.us-east-1.rds.amazonaws.com"
PORT="3306"
USER="mgsher"
REGION="us-east-1f"
DBNAME="cypher"
PASSWORD = "cypherteam"

conn = pymysql.connect(host="career-info.coid7kfjmyst.us-east-1.rds.amazonaws.com", user="mgsher", password="cypherteam",db="cypher")

cur = conn.cursor()
cur.execute("SELECT jobid,job_descript FROM tJobRaw;")
x = cur.fetchall()
#iter over every single job
for jobid, jobdesc in x:
    #use keywordloc function to find keywords in jobdesc
    Keys = Keyword(jobdesc)
    De =str(Keys[0])
    Te =str(Keys[1])
    Sk =str(Keys[2])
    Sp =int(Keys[3])
    jobid = int(jobid)
    print (Keys)

    insert_stmt = (
    "INSERT INTO tJobDesc (jobid, degree, tools, skillset,sponser) "
    "VALUES (%s, %s, %s, %s, %s)"
    )
    cust_params = (jobid, De,Te,Sk,Sp)
    cur.execute(insert_stmt, cust_params)

conn.commit()

conn.close()