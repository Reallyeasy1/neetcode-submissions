class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        op = []
        partition = []

        # j = start index of current substring
        # i = end index we are expanding into 
        def helper(j, i):
            if i >= len(s):
                if i == j:
                    op.append(partition[:])
                
                return
            
            if isPalindrome(s, j, i):
                partition.append(s[j: i + 1])
                helper(i + 1, i + 1)
                partition.pop()
            
            helper(j, i + 1)
        
        helper(0,0)
        return op
