def front_back(st):
  if len(st)>1:
    return st[len(st)-1]+st[1:(len(st)-1)]+st[0]
  return st