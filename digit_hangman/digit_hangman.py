def hangman(question, guess, board=None):
  if not board: 
    board = {
      "score": 0,
      "wrong": [],
      "secret": ["_" for x in question],
      "question": question,
      "num": 5,
      "status": "lose",
      "answer": []
    }

  # num decrease every round
  board['num'] -= 1

  # get index of current guess
  index = [x for x, y in enumerate(board["question"]) if y == guess]

  # current --> show secret and increase score
  for key in index:
    board["secret"][key] = guess
    board["score"] += 1
  
  # wrong --> add wrong guess to wrong
  if not len(index): board['wrong'].append(guess)


  # answer
  answer = " ".join(str(x) for x in board["secret"]) + " " + " ".join(str(x) for x in board["wrong"])
  board["answer"].append(answer)

  # checkpoint
  if board['num'] == 0:
    print(board["score"])
    return board

  # call recursive
  return hangman(question, int(input("Enter value: ")), board)


def user_input(test=False):
  question = input("Enter Question: ")
  question = [int(x) for x in question.split(" ")] # question string to list
  if len(question) < 12: return print("*Question must have 12 number")
  if len(question) > 12:  return print("*Question must have 12 number")
  if test: return # exist for test 


  result = hangman(question, int(input("Enter value: ")))

  # display
  print("\n".join(result['answer']))
  print(result["score"])

  

if __name__ == "__main__":
  user_input()