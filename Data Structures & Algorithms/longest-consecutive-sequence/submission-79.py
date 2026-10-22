class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet: 
            length = 0
            if (num-1) not in numSet: 
                length = 0
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0 
        for n in nums:
            if (n-1) not in numSet:
                length = 0
                while(n + length) in numSet:
                    length+=1
                longest = max(length, longest) 
        
        return longest
"""