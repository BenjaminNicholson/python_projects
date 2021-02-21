import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def find_definition(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        return f"did you mean {get_close_matches(w, data.keys())[0]} instead?"
    else:
        return "The word isn't listed in the dictionary. Please double check spelling"
  
word = input("Please enter a word to define: ").lower()




print(find_definition(word))

