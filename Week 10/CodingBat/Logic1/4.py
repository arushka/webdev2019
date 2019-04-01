def caught_speeding(speed, is_birthday):
  s=60
  f=80
  if is_birthday:
    s+=5
    f+=5
  if speed<=s:
    return 0
  elif f>=speed>=s+1:
    return 1
  return 2
