# Third LC problem May 19th


class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:

        starti = 0
        out = []

        while starti < len(nums) - 1:

            for i in range(starti, len(nums)-1):
                if nums[starti] + nums[i+1] == target:
                    out = [starti, i+1]

            starti += 1

        return out


test = Solution()

# Input: nums = [2,7,11,15], target = 9
print(test.twoSum(nums = [2,7,11,15], target = 9))
# Returns [0,1]

# Input: nums = [3,2,4], target = 6
print(test.twoSum(nums = [3,2,4], target = 6))
# Returns [1,2]

# Input: nums = [3,3], target = 6
print(test.twoSum(nums = [3,3], target = 6))
# Returns [0,1]

# Input: nums = [3,2,3], target = 6
print(test.twoSum(nums = [3,2,3], target = 6))
# Returns [0,2]
