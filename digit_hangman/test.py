import unittest
from unittest.mock import patch
import digit_hangman
import io
import sys

class TestHangman(unittest.TestCase):

  def test_question_less_than12(self):
    # capture print
    capturedOutput = io.StringIO()    
    sys.stdout = capturedOutput   

    with patch('builtins.input', side_effect="2 2 2 2 2 3 3 3 3 3 3"):
      stacks = digit_hangman.user_input(True)
    expected = "*Question must have 12 number\n"
    self.assertEqual(capturedOutput.getvalue(), expected)

  def test_question_more_than12(self):
    # capture print
    capturedOutput = io.StringIO()    
    sys.stdout = capturedOutput   
    
    expected = "*Question must have 12 number\n"
    with patch("builtins.input", side_effect=["2 2 2 2 2 3 3 3 3 3 3 3 3 3"]):
      stacks = digit_hangman.user_input(True)
    self.assertEqual(capturedOutput.getvalue(), expected)

  def test_show_secret1(self):
    question = "9 9 4 2 2 4 7 7 9 6 6 4"
    question = [int(x) for x in question.split(" ")] 
    guess = 9
    expected = question
    with patch("builtins.input", side_effect=["6", "7", "2", "4"]):
      stacks = digit_hangman.hangman(question, guess)['secret']
    self.assertEqual(expected, stacks)

  def test_show_secret1(self):
    question = "2 2 2 2 2 3 3 3 3 3 3 3"
    question = [int(x) for x in question.split(" ")] 
    guess = 2
    expected = question
    with patch("builtins.input", side_effect=["3", "4", "5", "6"]):
      stacks = digit_hangman.hangman(question, guess)['secret']
    self.assertEqual(expected, stacks)

if __name__ == '__main__':
    unittest.main()