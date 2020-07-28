def word_am(input):
  string=input.lower()
  string_split=string.split()
  instances=0
  for i in string_split:
    if i == "am":
      instances = instances+1
  return instances



  