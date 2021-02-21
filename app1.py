import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def find_definition(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        new_word = input(f"did you mean {get_close_matches(w, data.keys())[0]} instead? Enter Y if yes, or N if no: ").upper()
        if new_word == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif new_word == "N":
            return "The word isn't in this dictionary. Please double check entry"
        else:
            return "We didn't understand your entry"
    else:
        return "The word isn't listed in the dictionary. Please double check spelling"
  
word = input("Please enter a word to define: ").lower()

output = find_definition(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(find_definition(word))

