"""
second -> create a dictionary mapping for the number of decimal place 
to possible roman unique values in that range
"""
UNITMAPPING = {
  "1": ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
  "2": ["X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
  "3": ["C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
  "4": ["M", "MM", "MMM"]
}

def arabicToRoman(num: int) -> str:
  """
  first -> convert number to str and get length of number to determine 
  decimal place
  """
  numStr = str(num)
  length = len(numStr)
  lengthStr = str(length)

  """
  check if length < 1 or number is less than 1, to prevent infinite
  recursion
  """
  if length < 1 or num < 1:
    return ''

  """
  intermediate step -> check if length of number string is greater than 4
  or number itself is greater than 3999, if true raise exception
  """
  if length > 4 or num > 3999:
    raise Exception("Invalid input")

  """
  third -> using the dictionary map, find the appropriate value that 
  matches the number at each index using their decimal place
  """
  intOfFirstNum = int( numStr[0] )
  indexOfFirstNum = intOfFirstNum-1
  roman = UNITMAPPING[lengthStr][indexOfFirstNum]

  """
  fourth -> do step 3 - iteratively or recursively for the numbers 
  left in the string of numbers
  """
  numbersLeft = numStr[1:]
  
  roman += arabicToRoman( int(numbersLeft) )

  """
  return string
  """
  return roman

print(arabicToRoman(1789))