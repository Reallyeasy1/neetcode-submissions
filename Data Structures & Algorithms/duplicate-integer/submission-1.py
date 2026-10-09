class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ctr = {}

        for i in range(len(nums)):
            if nums[i] in ctr:
                return True

            else:
                ctr[nums[i]] = True

        return False