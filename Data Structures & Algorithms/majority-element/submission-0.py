class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur = nums[0]
        votes = 0

        for num in nums:
            if num == cur:
                votes += 1
            elif votes == 1:
                cur = num
            else:
                votes -= 1
        
        return cur