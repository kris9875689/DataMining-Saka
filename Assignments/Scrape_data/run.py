
# This code will gives all the departments list and professors lisy=t in the university named JNTU
import sys
import random
import requests
Name = []

file=open('result.csv','w+')
link = "http://jntuhceh.ac.in/faculty/4/dept" 
request = requests.get(link).text.split('\n')
for line in request:
    get = line.find('href="http://')
    if get>0:
        line = line[get:]
        pos = line.find('>')
        Name.append(line[pos+1: -3])
        file.write(line[pos+1: -3])
        file.write("\n")
        

print(Name)
