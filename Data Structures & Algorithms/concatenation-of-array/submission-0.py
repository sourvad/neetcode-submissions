class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        N = len(nums)

        if N < 1:
            return []

        ans = [0] * (N * 2)
        
        for i in range(N):
            ans[i] = nums[i]
            ans[i + N] = nums[i]

        return ans