import string

def sort_acronym(name):
  # validate
  if not name :return false

  abbrev = list(filter(lambda firstLetter: firstLetter[0].isupper(), name.split(" "))) # get word that have upper case in first letter
  abbrev = list(map(lambda firstLetter : firstLetter[0], abbrev)) # abbrev word

  return "".join(map(str, abbrev))

def main():
  # input number of input
  timeN = int(input("Enter number of times you want to run: "))
  answer = [] 

  # get input N time and find abbrev
  for time in range(timeN):
    answer.append(sort_acronym(input("Enter full state name: ")))

  # output
  print("\n".join(sorted(answer, key=len, reverse=True)))
    
main()