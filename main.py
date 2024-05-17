from collections import defaultdict

vstupni_text = input("Zadejte řetězce oddělené čárkami: ")
retezce = vstupni_text.split(', ')

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
   
for character in sorted(kategorie):
  printable_words = ""
  count = 1
  x = kategorie.get(character)
  
  for word in x:
    printable_words += word
    
    if count < len(x):
      printable_words += ", "

    count += 1
      
  print(f"{character}: {printable_words}")


