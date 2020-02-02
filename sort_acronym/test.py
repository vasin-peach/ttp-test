import unittest
import acronym_sort

class TestAcronym(unittest.TestCase):
  def test_lowercase_in_text(self):
    expected = "USA"
    actual = acronym_sort.acronym("United States of Americas")
    self.assertEqual(expected, actual)
    
  # space test
  def test_space_in_front(self):
    expected = "USA"
    actual = acronym_sort.acronym(" United States of Americas")
    self.assertEqual(expected, actual)
  def test_space_in_tail(self):
    expected = "USA"
    actual = acronym_sort.acronym("United States of Americas  ")
    self.assertEqual(expected, actual)
  def test_2more_space_between_word(self):
    expected = "USA"
    actual = acronym_sort.acronym("United  States   of   Americas  ")
    self.assertEqual(expected, actual)
  
class TestAcronymSort(unittest.TestCase):
  def test_abbrev_sort(self):
    expected = "TUSOA\nTUSA\nCMU"
    user_input = ["The United States of America",
      "The United States Of America", 
      "Carnegie Mellon University"]
    actual = acronym_sort.main(user_input)
    self.assertEqual(expected, actual)

class TestAcronymSort2(unittest.TestCase):
  def test_abbrev_sort(self):
    expected = "TUSOA\nTUSA\nCMU\nUSA\nA"
    user_input = ["the United States of America",
      "The United States of America", 
      "Carnegie Mellon University", 
      "The United States Of America",
      "the united states of America"]
    actual = acronym_sort.main(user_input)
    self.assertEqual(expected, actual)


    # actual = acronym_sort.main()

if __name__ == "__main__":
    unittest.main()