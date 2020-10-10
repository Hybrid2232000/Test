def solution( nums, k):
    nums.sort()
    return nums[-k]

print(solution([1,4,2,3,56,7,8,0,53,45,3], 4))