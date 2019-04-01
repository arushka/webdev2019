def count_evens(events):
  c=0
  for i in range(len(events)):
    if events[i]%2==0:
      c+=1
  return c