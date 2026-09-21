class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [6,7,8,1,2,3,4,5], left = 1, right = 6, mid = 3, target = 7
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid 

            # It is sorted from left to mid 
            if nums[left] <= nums[mid]:
                # Out of range, we search the other side
                if target > nums[mid] or target < nums[left]:
                    left = mid  + 1
                else: 
                    right = mid - 1

            # It is not sorted from left to mid, pivot is in between left and mid 
            else:
                # target is in between left and mid 
                if target < nums[mid] or target > nums[right]: 
                    right = mid - 1
                else: 
                    left = mid + 1
                
        return -1 