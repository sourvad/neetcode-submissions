class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, 0
        
        while r < len(nums):
            nums[l], nums[r] = nums[r], nums[l]
            r += 1

            if nums[l] != val:
                l += 1
        
        return l
