def alarm_clock(days, vacation):
  if vacation:
    if days==0 or days==6:
      return "off"
    return "10:00"
  else:
    if days==0 or days==6:
      return "10:00"
  return "7:00"