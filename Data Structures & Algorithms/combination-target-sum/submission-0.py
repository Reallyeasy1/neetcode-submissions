class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        op = []

        def dfs(i, currentList, total):
            if total == target:
                op.append(currentList[:])
                return
            if i >= len(nums) or total > target:
                return 
            
            else:
                currentList.append(nums[i])
                dfs(i, currentList, total + nums[i])
                currentList.pop()
                dfs(i + 1, currentList, total)

        dfs(0, [], 0)
        return op