import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# get raw data from the specified url
def get_soup(url):
    
    raw_data = requests.get(url)
    raw_data = raw_data.text
    soup = BeautifulSoup(raw_data, 'html.parser')
    return soup

# -----------------------------------
# code copied from 
# https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
import re
# as per recommendation from @freylis, compile once only
CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext
# ------------------------------------

# get list of company names in a given Indeed webpage
def get_company_name(soup):
    
    name_list = []
    
    for item in soup.find_all('a', attrs={'data-tn-element' : 'companyName'}):
        data_str = data_str + item.get_text()
        name_list.append(item.get_text())
    return name_list

def generate_list():
    url = "https://www.indeed.com/jobs?q=data%20scientist&l=Richmond%2C%20VA&vjk=be01cc7841e7b63c"
    output_list = []
    
    soup = get_soup(url)
    link_list = []
    for item in soup.find_all("div", {"id": "mosaic-provider-jobcards"}):
        for a in item.find_all('a', id = True):
            job_id = a['id']
            link_list.append(job_id.split("_",1)[1])
            
    description_text = []
    
    i = 0

    for link in link_list:
        job_url = "https://www.indeed.com/viewjob?jk="+link
        job_specific = requests.get(job_url)
        job_specific = job_specific.text
        job_soup = BeautifulSoup(job_specific, 'html.parser')

        for description in job_soup.find_all("div", {"id": "jobDescriptionText"}):
            #print(job_url)
            #print(cleanhtml(str(description)))
            #print("----------------------")
            output_list.append([i, job_url, cleanhtml(str(description))])
        
        i += 1
    return output_list

if __name__ == "__main__":
    generate_list()
            

#for iy in output_list:
    #print(iy[0])

#print(output_list)




