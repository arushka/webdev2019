def pos_neg(a, b, negative):
  if negative is True:
    if a<0 and b<0:
      return True
  else:
    if a*b<0:
      return True
  return False