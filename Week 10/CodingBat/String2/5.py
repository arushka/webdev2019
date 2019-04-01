def end_other(a, b):
  a=a.lower()
  b=b.lower()
  s=a
  f=b
  if len(a)>len(b):
    s=b
    f=a
  return f[len(f)-len(s):]==s
