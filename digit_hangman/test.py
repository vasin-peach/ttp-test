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

#   def test_hangman(self):
#     # capture print
#     capturedOutput = io.StringIO()  
#     sys.stdout = capturedOutput   
    
#     expected = "[
#       ""_ _ _ _ _ _ _ _ _ _ _ _",
#       "2 2 2 2 2 _ _ _ _ _ _ _"
#       "2 2 2 2 2 3 3 3 3 3 3 3"
#       "2 2 2 2 2 3 3 3 3 3 3 3 4"
#       "2 2 2 2 2 3 3 3 3 3 3 3 4 5"
#       "2 2 2 2 2 3 3 3 3 3 3 3 4 5 6"
#       "12""
#     ]"
#     with patch("builtins.input", side_effect=["2 2 2 2 2 3 3 3 3 3 3 3", "2", "3", "4", "5", "6"]):
#       stacks = digit_hangman.user_input(False)
#     self.assertEqual(capturedOutput.getvalue(), expected)




#     # actual = digit_hangman.user_input("2 2 2 2 2 3 3 3 3 3 3")
# if __name__ == '__main__':
#     unittest.main()