def last2(str):
  if len(str) < 2:
    return 0
  last2 = str[len(str)-2:]
  c = 0
  for i in range(len(str)-2):
    s = str[i:i+2]
    if s == last2:
      c = c + 1
  return c