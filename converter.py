def arabicToRoman(num: int) -> str:
  """
  first -> convert number to str and get length of number to determine 
  decimal place

  second -> create a dictionary mapping for the number of decimal place 
  to possible roman unique values in that range

  third -> using the dictionary map, find the appropriate value that 
  matches the number at each index using their decimal place

  fourth -> do step 3 - iteratively or recursively
  """
