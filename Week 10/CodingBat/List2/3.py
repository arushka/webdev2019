def centered_average(nums):
    maxi = max(nums)
    mini = min(nums)
    foundmaxi = False
    foundmini = False
    sum = 0
    c = 0
    for i in range(len(nums)):
        if nums[i] != maxi and nums[i] != mini:
            sum += nums[i]
            c += 1
        else:
            if foundmaxi and nums[i] == maxi:
                sum += maxi
                c += 1
            if foundmini and nums[i] == mini:
                sum += mini
                c += 1
            if not foundmaxi and nums[i] == maxi:
                foundmaxi = True
            if not foundmini and nums[i] == mini:
                foundmini = True
    return sum // c