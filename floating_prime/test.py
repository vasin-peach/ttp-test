import unittest
import floating_prime

class TestPrime(unittest.TestCase):
  def test_is_prime1(self):
    expected = True
    actual = floating_prime.prime(97)
    self.assertEqual(expected, actual)
  def test_is_prime2(self):
    expected = True
    actual = floating_prime.prime(83)
    self.assertEqual(expected, actual)
  def test_is_prime3(self):
    expected = True
    actual = floating_prime.prime(2)
    self.assertEqual(expected, actual)
  def test_not_prime1(self):
    expected = False
    actual = floating_prime.prime(100)
    self.assertEqual(expected, actual)
  def test_not_prime2(self):
    expected = False
    actual = floating_prime.prime(1)
    self.assertEqual(expected, actual)
  def test_not_prime3(self):
    expected = False
    actual = floating_prime.prime(55)
    self.assertEqual(expected, actual)
  def test_value_is_float(self):
    expected = False
    actual = floating_prime.prime(1.66753)
    self.assertEqual(expected, actual)

class TestFloatingPrime(unittest.TestCase):
  def test_answer1(self):
    expected = True
    actual = floating_prime.floating_prime(1.433183743)
    self.assertEqual(expected, actual)
  def test_answer2(self):
    expected = True
    actual = floating_prime.floating_prime(1.31234567)
    self.assertEqual(expected, actual)
  def test_answer3(self):
    expected = False
    actual = floating_prime.floating_prime(1.6172746483)
    self.assertEqual(expected, actual)
  def test_answer3(self):
    expected = ""
    actual = floating_prime.floating_prime(0.0)
    self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()