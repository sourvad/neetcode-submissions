class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        seen = set()
        l, r = 0, 0

        while r < len(nums):
            if nums[r] in seen:
                return True
            
            if r - l == k:
                seen.remove(nums[l])
                l += 1
           
            seen.add(nums[r])
            r += 1
            
        
        return False