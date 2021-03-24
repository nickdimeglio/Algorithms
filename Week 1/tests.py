# TESTS FOR MULTIPLICATION ALGORITHMS ARE HERE
from multiplication import recursive, karatsuba
import unittest


class TestMultiplication(unittest.TestCase):
	"""Test our multiplication algorithms"""

	def test_recursive(self):
		
		ans1 = 7 * 9
		self.assertEqual(ans1, recursive(7, 9))

		ans2 = 12345678 * 87654321
		self.assertEqual(ans2, recursive(12345678, 87654321))

	def test_karatsuba(self):
	
		ans1 = 8 * 2
		self.assertEqual(ans1, karatsuba(8, 2))
	
		ans2 = 12345678 * 87654321
		self.assertEqual(ans2, karatsuba(12345678, 87654321))

if __name__ == '__main__':
	unittest.main()

