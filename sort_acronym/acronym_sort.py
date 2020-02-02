def acronym(name):
  # validate
  if not name :return false

  abbrev = list(filter(lambda firstLetter: firstLetter[0].isupper() if len(firstLetter) else False, name.split(" "))) # get word that have upper case in first letter
  abbrev = list(map(lambda firstLetter : firstLetter[0], abbrev)) # abbrev word

  return "".join(map(str, abbrev))

def main(data):
  
  answer = [] 

  if data: # for test

    for text in data:
      answer.append(acronym(text))
      
    return "\n".join(sorted(answer, key=lambda x: (-len(x),x)))

  else: # for user

    # input number of input
    timeN = int(input("Enter number of times you want to run: "))
    # get input N time and find abbrev
    for time in range(timeN):
      answer.append(acronym(input("Enter full text name: ")))
    # output
    print("\n".join(sorted(answer, key=lambda x: (-len(x),x))))
    
if __name__ == '__main__':
  main(None)