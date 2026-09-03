class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = len(nums)
        l = 0

        while l < r:
            if nums[l] == val:
                nums[l] = nums[r - 1]
                r -= 1
            else:
                l += 1

        return r
    