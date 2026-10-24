"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Input: 
            nums list
            target sum of two values
        Output: 
            list of indices
        '''
        # access target, minus the first value from it
        # see if you can find the value that is subtracted in the rest of the array
        # if yes, terminate and return index
        # if no, keep going
        
        temp = 0
        y_index = 0
        for i in nums:
            temp = target - i
            print(i, nums.index(i))
            if temp in nums and nums.index(temp) != nums.index(i): 
                print(temp, nums.index(temp))
                y_index = nums.index(temp)
                break
        return [nums.index(i), y_index]
        '''
        temp = 0
        y_index = 0

        for x_index, i in enumerate(nums):
            temp = target - i
            
            if temp in nums[x_index + 1:]:
                y_index = nums.index(temp, x_index + 1)
                break

        return [x_index, y_index]
        '''
"""



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Input: 
            nums list
            target sum of two values
        Output: 
            list of indices
        """
        sum_nums = []
        for i in range(len(nums)-1,-1, -1):
            diff = target - nums[i]
            if diff in nums:
                sum_nums.append(nums.index(diff))
                sum_nums.append(i)
                break
        return sum_nums

        


