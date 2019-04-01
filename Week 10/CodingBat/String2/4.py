def count_code(str):
  c=0
  for i in range(len(str)-3):
    if str[i:i+2]=="co" and str[i+3]=="e":
      c+=1
  return c