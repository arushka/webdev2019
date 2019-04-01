def rotate_left3(nums):
  c=nums[0]
  nums.remove(nums[0])
  nums.append(c)
  return nums