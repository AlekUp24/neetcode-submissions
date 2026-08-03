class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resMap = {}

        for i in range(len(nums)):
            resMap[nums[i]] = i
        
        for i in range(len(nums)):
            seek = target - nums[i]
            if seek in resMap and resMap[seek] != i:
                return [i, resMap[seek]]
        
        return []