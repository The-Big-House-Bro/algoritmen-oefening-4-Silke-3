
def countTargetPairs(nums, target):
    pairs = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] < target:
                pairs += 1
    return pairs

nums = [6, -6, -7, 2, 3]
target = 2
result = countTargetPairs(nums, target)
print(result)
