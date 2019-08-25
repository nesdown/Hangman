import requests
from bs4 import BeautifulSoup
from random import randint

def return_random_word():
  try:
    url = "https://www.vocabulary.com/lists/33" + str(randint(100, 150))

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    random_word = soup.find_all("a", {"class" : "word dynamictext"})[0]

    print("Word found successfully!\n")
    print("*" * len(random_word.text))
    return random_word.text

  except:
    print("There were no words, trying again...")
    return_random_word()
