import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json

import urllib.request
request_url = urllib.request.urlopen('https://ipinfo.io/json')
a=json.load(request_url)
city=a['city']
print(city)
url =requests.get("http://api.weatherapi.com/v1/history.json?key=46242b3221204e6ca2d143019221012&q="+city+"&dt=2022-12-5")
data=url.json()
date=data['forecast']['forecastday'][0]['date']
day=data['forecast']['forecastday'][0]['day']
maxtemp_c1=day['maxtemp_c']
mintemp_c1=day['mintemp_c']
avgtemp_c1=day['avgtemp_c']
maxtemp_f1=day['maxtemp_f']
mintemp_f1=day['mintemp_f']
avgtemp_f1=day['avgtemp_f']
maxwind_mph1=day['maxwind_mph']
maxwind_kph1=day["maxwind_kph"]
url =requests.get("http://api.weatherapi.com/v1/history.json?key=46242b3221204e6ca2d143019221012&q="+city+"&dt=2022-12-6")
data=url.json()
date=data['forecast']['forecastday'][0]['date']
day=data['forecast']['forecastday'][0]['day']
maxtemp_c2=day['maxtemp_c']
mintemp_c2=day['mintemp_c']
avgtemp_c2=day['avgtemp_c']
maxtemp_f2=day['maxtemp_f']
mintemp_f2=day['mintemp_f']
avgtemp_f2=day['avgtemp_f']
maxwind_mph2=day['maxwind_mph']
maxwind_kph2=day["maxwind_kph"]
url =requests.get("http://api.weatherapi.com/v1/history.json?key=46242b3221204e6ca2d143019221012&q="+city+"&dt=2022-12-7")
data=url.json()
date=data['forecast']['forecastday'][0]['date']
day=data['forecast']['forecastday'][0]['day']
maxtemp_c3=day['maxtemp_c']
mintemp_c3=day['mintemp_c']
avgtemp_c3=day['avgtemp_c']
maxtemp_f3=day['maxtemp_f']
mintemp_f3=day['mintemp_f']
avgtemp_f3=day['avgtemp_f']
maxwind_mph3=day['maxwind_mph']
maxwind_kph3=day["maxwind_kph"]
url =requests.get("http://api.weatherapi.com/v1/history.json?key=46242b3221204e6ca2d143019221012&q="+city+"&dt=2022-12-8")
data=url.json()
date=data['forecast']['forecastday'][0]['date']
day=data['forecast']['forecastday'][0]['day']
maxtemp_c4=day['maxtemp_c']
mintemp_c4=day['mintemp_c']
avgtemp_c4=day['avgtemp_c']
maxtemp_f4=day['maxtemp_f']
mintemp_f4=day['mintemp_f']
avgtemp_f4=day['avgtemp_f']
maxwind_mph4=day['maxwind_mph']
maxwind_kph4=day["maxwind_kph"]
url =requests.get("http://api.weatherapi.com/v1/history.json?key=46242b3221204e6ca2d143019221012&q="+city+"&dt=2022-12-9")
data=url.json()
date=data['forecast']['forecastday'][0]['date']
day=data['forecast']['forecastday'][0]['day']
maxtemp_c5=day['maxtemp_c']
mintemp_c5=day['mintemp_c']
avgtemp_c5=day['avgtemp_c']
maxtemp_f5=day['maxtemp_f']
mintemp_f5=day['mintemp_f']
avgtemp_f5=day['avgtemp_f']
maxwind_mph5=day['maxwind_mph']
maxwind_kph6=day["maxwind_kph"]
tempc={'maxtemp':[maxtemp_c1,maxtemp_c2,maxtemp_c3,maxtemp_c4,maxtemp_c5],
      'avgtemp':[avgtemp_c1,avgtemp_c2,avgtemp_c3,avgtemp_c4,avgtemp_c5],
      'mintemp':[mintemp_c1,mintemp_c2,mintemp_c3,mintemp_c4,mintemp_c5]}
tempcs=pd.DataFrame(tempc,index=['2022-12-5','2022-12-6','2022-12-7','2022-12-8','2022-12-9'])
print(tempcs)
plt.plot(tempcs)
plt.title('Celsius')
plt.ylabel('Temperature ')
plt.legend(['Maxtemp','Avgtemp','Mintemp'])
plt.xlabel('Date')
plt.show()
tempf={'maxtemp':[maxtemp_f1,maxtemp_f2,maxtemp_f3,maxtemp_f4,maxtemp_f5],
      'avgtemp':[avgtemp_f1,avgtemp_f2,avgtemp_f3,avgtemp_f4,avgtemp_f5],
      'mintemp':[mintemp_f1,mintemp_f2,mintemp_f3,mintemp_f4,mintemp_f5]}
tempfs=pd.DataFrame(tempf,index=['2022-12-5','2022-12-6','2022-12-7','2022-12-8','2022-12-9'])
print(tempfs)
plt.plot(tempfs)
plt.title('Farenheit')
plt.ylabel('Temperature ')
plt.legend(['Maxtemp','Avgtemp','Mintemp'])
plt.xlabel('Date')
plt.show()