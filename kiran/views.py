import pandas as pd
import requests
from django.shortcuts import render
from django.core.mail import send_mail
from pandas import option_context

from django.conf import settings
from django.core.mail import send_mail

import base64
import requests  # to make TMDB API calls
import io
import pandas
import base64
import matplotlib.pyplot as plt

columns = ['film', 'revenue']

df = pandas.DataFrame(columns=columns)
def kiran(request):
    api_key = "3386c9158e908c7c2260890dda5fd20a"
    base_url = "https://api.themoviedb.org/3"

    r = requests.get(f"{base_url}/movie/popular", params={'api_key': api_key})

    data = r.json()
    dict1 = {}

    for movie in data["results"]:
        title = movie['title']
        overview = movie['overview']
        posterpath = movie['poster_path']
        receive = requests.get('https://image.tmdb.org/t/p/original/' + posterpath)
        image = base64.b64encode(receive.content).decode('utf-8')
        dict1.update({'title'+title: title, 'overview'+title : overview,'posterpath'+title: image})
        data={'data':dict1}
    return render(request,'movies.html',data)
    





    


def movie_analysis(request):
    receive = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=3386c9158e908c7c2260890dda5fd20a')
    data = receive.json()

    for i in data["results"]:
        film_revenue = requests.get('https://api.themoviedb.org/3/movie/' + str(
            i['id']) + '?api_key=3386c9158e908c7c2260890dda5fd20a&primary_release_year=2017&sort_by=revenue.desc')
        data = film_revenue.json()
        if data['revenue'] != 0:
            df.loc[len(df)] = [i['title'], data['revenue']]
    x = df['film']
    y = df['revenue']
    data = pandas.DataFrame(df).to_html()
    plt.figure(figsize=(15, 10))
    plt.plot(x, y)
    plt.grid(axis='y')
    plt.xlabel('movie-name',fontsize=50)
    plt.ylabel('collection',fontsize=50)
    image2 = io.BytesIO()
    plt.savefig(image2, format="png", dpi=800)
    image2 = base64.b64encode(image2.getvalue()).decode('utf-8').replace('\n', '')
    data = {'image': image2, 'data': data}
    return render(request,'movie-analysis.html',data)

    
    for j in data["results"]:
        film_revenue = requests.get('https://api.themoviedb.org/3/movie/' + str(
            j['id']) + '?api_key=3386c9158e908c7c2260890dda5fd20a & original_language=tel& primary_release_year=2017&sort_by=revenue.desc ')
        data = film_revenue.json()
        if data['revenue'] != 0:
            df.loc[len(df)] = [j['title'], data['revenue']]
    x = df['film']
    y = df['revenue']
    data = pandas.DataFrame(df).to_html()
    plt.figure(figsize=(15, 10))
    plt.plot(x, y)
    plt.grid(axis='y')
    plt.xlabel('movie-name',fontsize=50)
    plt.ylabel('collection',fontsize=50)
    image2 = io.BytesIO()
    plt.savefig(image2, format="png", dpi=800)
    image2 = base64.b64encode(image2.getvalue()).decode('utf-8').replace('\n', '')
    data = {'image': image2, 'data': data}
    return render(request,'movie-analysis.html',data)

    

def genre(request):
    api_key = "3386c9158e908c7c2260890dda5fd20a"
    base_url = "https://api.themoviedb.org/3"
    r = requests.get(f"{base_url}/movie/popular", params={'api_key': api_key})
    data=r.json()
    ka=[]
    ap=[]
    ma=[]
    sa=[]
    a=data['results']
    for i in a: 
        for j , k in i.items():
            if j == 'original_title':
                ka.append(k)
            if j =='release_date':
                ap.append(k)
            if j =='vote_average':
                ma.append(k)
            if j =='vote_count':
                sa.append(k)
    m={"Movie_title":ka,"relesed_year":ap,"rating":ma,"vote_count":sa}
    pd.set_option('display.max_colwidth',None)
    df=pd.DataFrame(m,index=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]).to_html()
    x = ma
    y = sa
    plt.figure(figsize=(15, 10))
    plt.plot(x, y)
    plt.grid(axis='y')
    plt.xlabel('rating',fontsize=50)
    plt.ylabel('vote_count',fontsize=50)
    image2 = io.BytesIO()
    plt.savefig(image2, format="png", dpi=800)
    image2 = base64.b64encode(image2.getvalue()).decode('utf-8').replace('\n', '')
    data = {'image': image2, 'data': df}
    return render(request,'genre.html',data)

    
    from tmdbv3api import TMDb
    from tmdbv3api import Movie
    tmdb = TMDb()
    tmdb.api_key = '3386c9158e908c7c2260890dda5fd20a'
    tmdb.language = 'en'
    tmdb.debug = True

    movie = Movie()
    # for example the movie with id=862
    m = movie.details()
    


def review(request):
        return render(request,'analysis.html')

        



    



            
    
    







