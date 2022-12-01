import requests

url = 'https://dog.ceo/api/breeds/image/random'

def main():
  req = requests.get(url)
  j = req.json()
  print(j)

main()