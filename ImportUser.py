import pymysql
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
my_text = docx2txt.process("/Users/helennayin/Documents/cypher/Yueyue Yin_resume.docx")
#iter over every single job
Key = Keyword(my_text)

def userfeed(Keys,Sponser = False):
    
    De =str(Keys[0])
    Te =str(Keys[1])
    Sk =str(Keys[2])
    Sp = int(Sponser)

    insert_stmt = (
    "INSERT INTO tCust (degree, tools, skillset,sponser) "
    "VALUES (%s, %s, %s, %s)"
    )
    cust_params = (De,Te,Sk,Sp)
    cur.execute(insert_stmt, cust_params)
userfeed(Key,True)
conn.commit()
conn.close()