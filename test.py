import unittest
from converter import arabicToRoman


class TestArabicToRomain(unittest.TestCase):

  def test_valid_input_value(self):
    self.assertEqual( arabicToRoman(9), 'IX' )
    self.assertEqual( arabicToRoman(79), 'LXXIX' )
    self.assertEqual( arabicToRoman(299), 'CCXCIX' )
    self.assertEqual( arabicToRoman(650), 'DCL' )
    self.assertEqual( arabicToRoman(1797), 'MDCCXCVII' )
    self.assertEqual( arabicToRoman(1889), 'MDCCCLXXXIX' )

  def test_invalid_input_exception(self):
    # check that arabicToRoman function raises exceptions 
    # when input is a string
    with self.assertRaises(TypeError):
      arabicToRoman('4000')
    # check that arabicToRoman function raises exceptions
    # for values greater than 3999
    with self.assertRaises(ValueError):
      arabicToRoman(4000)

if __name__ == '__main__':
  unittest.main()
