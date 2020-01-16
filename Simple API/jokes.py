import requests
from random import choice
url = 'https://icanhazdadjoke.com/search'
user_input = input("Enter a key for searching jokes: ? \n")

res = requests.get(url,
                   headers={"Accept": "application/json"},
                   params={'term': user_input}).json()
total_jokes = res['total_jokes']
result = res['results']

if total_jokes > 1:
    print(f"There are {total_jokes} number of jokes for this input ")
    print(f"Here  is one of them \n {choice(result)['joke']}")
elif total_jokes == 1:
    print(f"There is only one joke for this input \n Here it is \n {result[0]['joke']}\n")
else:
    print(" Sorry no jokes found for this input  :(")


