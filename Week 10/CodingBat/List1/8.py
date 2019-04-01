def max_end3(nums):
  arr=[]
  for i in range(3):
    arr.append(max(nums[0],nums[len(nums)-1]))
  return arr