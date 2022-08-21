'''Given an array of strings strs, group the anagrams together. 
You can return the answer in any order. An Anagram is a word or phrase formed by 
rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.'''


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict = {}
        for word in strs:
            key = tuple(sorted(word))
            dict[key] = dict.get(key, []) + [word]
        print(dict.values())
        
            
if __name__ == '__main__':

    strs = ["eat","tea","tan","ate","nat","bat"]
   
    test = Solution()
    test.groupAnagrams(strs)