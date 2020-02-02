import math

def prime(number):
  number = math.floor(number)

  # prime must grater than 1
  if number <= 1: return False
  for i in range(2, number):
    if (number % i ) == 0:
      return(False)
  return True

def floating_prime(number):

  # number must grater than 0
  if number < 1: return ""

  # find prime in demical 1, 2, 3
  for i in [10, 100, 1000]:
    if prime(i * number): return True 

  return False


if __name__ == '__main__':
  print(floating_prime(float(input("Enter Value: "))))