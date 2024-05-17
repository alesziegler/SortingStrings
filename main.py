from collections import defaultdict

# Požádání uživatele o vstup
vstupni_text = input("Zadejte řetězce oddělené čárkami: ")
retezce = vstupni_text.split(',')

# Vytvoření defaultdict pro kategorizaci řetězců
kategorie = defaultdict(list)
# Zde dokonči úlohu svým kódem...

#ok, in retezce, we have a list of strings.
#now we need to make keys out of the first character of every string
#what if we have two strings with the same first sign?
#well then the second string will be the second item on a list, 
#which is a value of a dictionary.

for word in retezce:
  try:
    int(word[0])
    kategorie["čísla"].append(word)
  except ValueError:
    first_character = word[0]
    kategorie[first_character].append(word)

sorted_kategorie = sorted(kategorie)

print(kategorie)

print(sorted_kategorie)

def list_items(list):
  for item in list:
    print(item,end=",")
    

for character in sorted(kategorie):
  printable_words = ""
  for word in kategorie.get(character):
    printable_words += word
  print(f"{character} : {kategorie.get(character)}")
  print(printable_words)