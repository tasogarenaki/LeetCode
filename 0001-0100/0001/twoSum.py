from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}                                    
        for i, num in enumerate(nums):              
            targ_num = target - num                 
            if targ_num in dic:                     
                return [dic[targ_num], i]           
            dic[num] = i                            

# Test
nums = [2, 7, 11, 15]
target = 9

solution = Solution()

print(solution.twoSum(nums, target))
