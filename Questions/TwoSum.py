"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return self.solution2(nums, target)

    def solution1(self, nums, target):
        for i in range(0, len(nums)):
            if i == len(nums) - 1:
                break
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # better solution using dictionary
    def solution2(self, nums, target):
        if len(nums) <= 1:
            return False
        cache = {}
        for i in range(0, len(nums)):
            if nums[i] in cache:
                return [cache[nums[i]], i]
            else:
                cache[target - nums[i]] = i

def main():
    nums = [2, 7, 11, 15]
    target = 26
    solution = Solution()
    result = solution.twoSum(nums, target)
    print result

if __name__ == '__main__':
    main()