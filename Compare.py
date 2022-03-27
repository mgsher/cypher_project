import pymysql

def parse(x):
  if x == None:
    return []
  else:
    return list(x.split(","))

def Compare(JD,candidate):
  score = 0
  scoreall = 3
  warnings = []
  if JD[4] == True and candidate[4] == 1:
    return 0

  else:
    degree = parse(JD[1])
    canddegree = parse(candidate[1])
    if len(degree) == 0:
      pass
      scoreall -= 1
    elif canddegree  in degree or (canddegree  == degree):
      score += 1
  
    else:
      warnings.append('However, Your education backgroud does not match this position')
    
    #parse string item by ,
    skill = parse(JD[2])
    candskill = parse(candidate[2])
    skillscore = 0
    skillall = len(skill)
    if skillall == 0:
      pass
      scoreall -= 1
    else: 
      for i in skill:
        if i in candskill:
          skillscore += 1
      score += (skillscore/skillall)  
      if (skillscore/skillall) < 0.5:
        warnings.append('However, Your techinical skills do not match this position')
    
    skset = parse(JD[3])
    candskset = parse(candidate[3])
    sksetscore = 0
    sksetall = len(skset)
    if sksetall == 0:
      pass
      scoreall -= 1
    else: 
      for i in skset:
        if i in candskset:
          sksetscore += 1
      score += (sksetscore/sksetall) 
      if (sksetscore/sksetall) < 0.5:
        warnings.append('However, Your skill sets do not match this position') 
    
   

    if score == 0:
      return 0
    else:
      return str(round(score/scoreall*100))+'%', warnings, JD[0]

if __name__ == "__main__":
    ENDPOINT="career-info.coid7kfjmyst.us-east-1.rds.amazonaws.com"
    PORT="3306"
    USER="mgsher"
    REGION="us-east-1f"
    DBNAME="cypher"
    PASSWORD = "cypherteam"

    conn = pymysql.connect(host="career-info.coid7kfjmyst.us-east-1.rds.amazonaws.com", user="mgsher", password="cypherteam",db="cypher")


    cur = conn.cursor()
    request = '???'
    request = int(request)
    select = ("SELECT * FROM tCust WHERE custid = %s;")
    cur.execute(select, request)
        
    x = cur.fetchall()
    user = x[0]
    cur.execute("SELECT * FROM tJobDesc") 
    y = cur.fetchall()

    for i in y:
        if Compare (i,user) == 0:
            pass
        else:
            MatchScore, Warning, JobID = Compare (i,user)
            id = int(JobID)
            select = ("SELECT job_url FROM tJobRaw WHERE jobid = %s;")
            cur.execute(select, id)
            url = cur.fetchone()
            MatchScore = ''.join(MatchScore)
            Warning = ' '.join(Warning)
            print('You are '+MatchScore+' match to this job, ', Warning, '\n','Apply Job'+str(url))

          
    conn.close()


