class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 0
        k = 0
        
        while cur < len(nums):
            while cur != len(nums) - 1 and nums[cur] == nums[cur + 1]:
                cur += 1
            
            nums[k] = nums[cur]
            cur += 1
            k += 1

        return k