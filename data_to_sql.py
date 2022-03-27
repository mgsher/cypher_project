import pymysql

from db_scraping import generate_list

data = generate_list()

ENDPOINT="career-info.coid7kfjmyst.us-east-1.rds.amazonaws.com"
PORT="3306"
USER="mgsher"
REGION="us-east-1f"
DBNAME="cypher"
PASSWORD = "cypherteam"

#conn = pymysql.connect(host="career-info.coid7kfjmyst.us-east-1.rds.amazonaws.com", user="mgsher", password="cypherteam",db="cypher")
conn = pymysql.connect(host=ENDPOINT, user=USER, password=PASSWORD,db=DBNAME)

cur = conn.cursor()
#cur.execute("select @@version")
#cur.execute("SHOW CREATE TABLE tCust;")
#cur.execute("""DROP TABLE IF EXISTS tCust""")
#cur.execute("""CREATE TABLE tCust(
#                    custid INTEGER PRIMARY KEY,
 #                   degree TEXT NOT NULL,
 #                   tools TEXT NOT NULL,
  #                  skillset TEXT NOT NULL,
  #                  sponser INTEGER NOT NULL
   #                 );""")


cur.execute("""DROP TABLE IF EXISTS tJobRaw""")
cur.execute("""CREATE TABLE tJobRaw(
                   jobid INTEGER PRIMARY KEY,
                   job_url TEXT NOT NULL,
                   job_descript TEXT NOT NULL
                   );""")
#cur.execute("select * from tJobRaw;")

insert_query = ("INSERT INTO tJobRaw (jobid, job_url, job_descript) VALUES (%s, %s, %s)")
#data = db_scraping.output_list
try:
    cur.executemany(insert_query, data)
except:
    print("Unable to populate the raw job data table.")
conn.commit()


cur.execute("select * from tJobRaw;")
output = cur.fetchall()
print(output)
   
# To close the connection
conn.close()