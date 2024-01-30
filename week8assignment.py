import numpy as np
import pandas as pd
import json
import requests
from bs4 import BeautifulSoup as BS


#open file and print it 
#f = open("hello.txt", "r")
#print(f.read())

#y = open("hellox2.txt", "r")
#for x in y:
#    print(x)

#simple for loop 
#for i in range (5): 
#    print(i)

#for i in range(2):
#    for j in range(4):
#            print(i,j)


print("Assignment 1") 
x = 1
for i in range (3):
    w = 101
    for y in range(5):
        print(w, end=" ")
        w = w+1

print("Assignment 2, a and b")
#first reading file
with open('sample2.json', 'r') as f:
    json_results = json.load(f)
    json_results2 = pd.read_json("sample2.json")

#converting this to a pandas Dataframe
data = pd.DataFrame(json_results)
data2 = pd.DataFrame(json_results2)
print(data)
print(data2)
f.close()

print("Assignment 3")
#link = "https://www.yelp.com"
search = 'restaurants'
loc = 'taipei'
path = f"https://www.yelp.com/search?cflt={search}s&find_loc={loc}]"
response = requests.get(path)
print (response.status_code)
print (response.content)

print("Assignment 4")
#    print(item)
SOUP = BS(response.content, 'html.parser')
element_list  = (SOUP.find_all('p'))
for element in element_list:
    print(element)