import random

def first():

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes)
  rnd = random.randint(0,last)
  print(quotes[rnd])

if __name__== "__main__":
  first()
