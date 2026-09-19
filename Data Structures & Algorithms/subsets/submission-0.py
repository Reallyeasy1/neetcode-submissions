class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        op = []
        subset = []

        def helper(i):
            if i >= len(nums):
                op.append(subset[:])
                return
            
            else:
                subset.append(nums[i])
                helper(i + 1)
                subset.pop()
                helper(i + 1)

        helper(0)
        return op

