def has22(nums):
  if len(nums)>=2:
    for i in range(len(nums)-1):
      if nums[i]==2 and nums[i+1]==2:
        return True
  return False