def containsCloseNums(nums, k):
    numIndexDict = {}
    numsLength = len(nums)
    for i in range(numsLength):
        if not nums[i] in numIndexDict.keys():
            numIndexDict[nums[i]] = i
        else:
            diff = i-numIndexDict[nums[i]]
            if diff <= k:
                return True
            elif diff > k:
                if i+k < numsLength:
                    numIndexDict[nums[i]] = i
    return False
