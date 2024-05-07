import pymongo as pm
import io
from PIL import Image
import base64
import requests
client=pm.MongoClient()
db=client['kiran']
a=db.kiran.insert_one({'username':'kiran','password':'kiran'})
#a=db.adarsh.insert_one({'1':1})  #mongodb insert one command
b=db.adarsh.find() #mongodb find command


class DB():
    def insertOne(self,key,value):
        db.adarsh.insert_one({key:value})
    def find(self,key,value):
        a=db.adarsh.find({key:value})
        for i in a:
            return i
    def image(self):
        receive = requests.get('https://image.tmdb.org/t/p/original//pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg')
        image2 = base64.b64encode(receive.content).decode("utf-8")
        return image2


from tmdbv3api import TMDb
tmdb=TMDb()
tmdb.api_key='3386c9158e908c7c2260890dda5fd20a'




'''
from tmdbv3api import TMDb
from tmdbv3api import Movie
tmdb=TMDb()
TMDb.api_key='3386c9158e908c7c2260890dda5fd20a'
movie=Movie()

import io
from PIL import Image
import base64
import requests
receive = requests.get('https://image.tmdb.org/t/p/original//pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg')
image2 = base64.b64encode(receive.content)
print(image2)
with open(r'E:\image5.png','wb') as f:
    f.write(receive.content)
import requests # to make TMDB API calls
import io
import pandas
import base64
import matplotlib.pyplot as plt

receive = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=3386c9158e908c7c2260890dda5fd20a')
data = receive.json()
columns = ['film', 'revenue']

df = pandas.DataFrame(columns=columns)

for i in data["results"]:
    film_revenue = requests.get('https://api.themoviedb.org/3/movie/'+str(i['id'])+'?api_key=3386c9158e908c7c2260890dda5fd20a&primary_release_year=2017&sort_by=revenue.desc')
    data=film_revenue.json()
    if data['revenue'] !=0:
        df.loc[len(df)]=[i['title'],data['revenue']]
x=df['film']
y=df['revenue']
plt.plot(x,y)
plot=plt.figure(figsize=(100,100))
image2 = io.BytesIO()
plot.savefig(image2, format="png")
image2 = base64.b64encode(image2.getvalue()).decode("utf-8")
print(image2)




