def array_front9(nums):
  if len(nums)>4:
    nums=nums[:4]
  for i in range(len(nums)):
    if nums[i]==9:
      return True
  return False