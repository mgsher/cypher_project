import pymysql

ENDPOINT="career-info.coid7kfjmyst.us-east-1.rds.amazonaws.com"
PORT="3306"
USER="mgsher"
REGION="us-east-1f"
DBNAME="cypher"
PASSWORD = "cypherteam"

# connect to the remote database
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

# To close the connection
conn.close()