'''Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.'''


class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]


if __name__ == '__main__':
    nums = [2,2,0,2,0,3,4]
    target = 7

    test = Solution()
    print(test.twoSum(nums, target))