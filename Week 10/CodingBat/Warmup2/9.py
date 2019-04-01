def string_match(a, b):
  s = min(len(a), len(b))
  c = 0
  for i in range(s-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      c = c + 1

  return c