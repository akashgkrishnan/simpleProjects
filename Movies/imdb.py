import requests
url = 'https://movie-database-imdb-alternative.p.rapidapi.com/'
movie_name = input("Enter the name of the movie: ")

headers = {
    'x-rapidapi-host': "movie-database-imdbm",
    'x-rapidapi-key': "e5713053ecm44"
    }
res = requests.get(url,
                   headers=headers,
                   params={"s": {movie_name}, "r": "json", "type": "movie"}).json()
search = res['Search']
print(f" A total of {res['totalResults']} ")
for i in range(int(res['totalResults'])):
    print(f"Title {search[i]['Title']} \n Year of Release {search[i]['Year']} \n ")
