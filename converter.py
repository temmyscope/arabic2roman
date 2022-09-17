def arabicToRoman(num: int) -> str:
  """
  first -> convert number to str and get length of number to determine 
  decimal place

  second -> create a dictionary mapping for the number of decimal place 
  to possible roman unique values in that range

  intermediate step -> check if length of number string is greater than 4
  or number itself is greater than 3999, if true raise exception

  third -> using the dictionary map, find the appropriate value that 
  matches the number at each index using their decimal place

  fourth -> do step 3 - iteratively or recursively
  """
