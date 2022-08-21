'''Given an integer array nums, return true if any value appears 
at least twice in the array, and return false if every element is distinct. '''

class Solution(object):
    def containsDuplicate(self, nums):
        if len(nums) != len(set(nums)):
            return True
        else:
            return False

if __name__ == '__main__':
    nums = [1,4,3,4]
    a = Solution()
    print(a.containsDuplicate(nums))

