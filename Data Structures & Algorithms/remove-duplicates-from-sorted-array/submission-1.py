class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = 0
        k = 1
        
        for cur in range(1, len(nums)):
            if nums[cur] == nums[cur - 1]:
                cur += 1
            else:
                nums[k] = nums[cur]
                k += 1

        return k
