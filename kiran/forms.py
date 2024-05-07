import pandas as pd
import requests

def movie_analysis(request):
    receive = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=3386c9158e908c7c2260890dda5fd20a')
    data = receive.json()

    for i in data["results"]:
        film_revenue = requests.get('https://api.themoviedb.org/3/movie/' + str(
            i['id']) + '?api_key=3386c9158e908c7c2260890dda5fd20a&primary_release_year=2017&sort_by=revenue.desc')
        data1 = film_revenue.json()
    print(data1)
