'''Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, 
return -1. You must write an algorithm with O(log n) runtime complexity.'''


class Solution(object):
    def search(self, nums, target):
        for i in nums:
            if i == target:
                location = nums.index(target)
                return location
        return -1

        

if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 9

    test = Solution()
    print(test.search(nums, target))