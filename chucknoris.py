import json
import csv
import requests
import pandas as pd
tests=pd.read_csv("ID.csv").values #file used to get th ids from
jokes=[]
ids=[]
result=""
for i in tests:
    url="http://api.icndb.com/jokes/{}".format(int(i))
    r=requests.get(url)
    joke=json.loads(r.content)['value']['joke']
    id=json.loads(r.content)["value"]['id']
    jokes.append(joke)
    ids.append(id)
    #result+="{},".format(i)+joke+"\n"
df=pd.DataFrame({"ID":ids,"Joke":jokes})
df.to_csv("apis.csv",index=False)
#if the len of both lists are not equal an error will occur
print(len(ids)) 
print(len(jokes))
#Another way of writing files using placeholders
"""""""""""""""""
  result+="{},".format(i)+joke+"\n"
    result=result[:-1]
    #print(result)
    with open("apis.csv","w",newline="") as f:
    f.write(result)
      
   """"""""""""""""""""
