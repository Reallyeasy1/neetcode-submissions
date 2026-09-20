class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        curr_tbl = {} # Stores sorted(str) : [list of strs]
        op = []

        for i in range(len(strs)):
            curr = strs[i]
            sorted_curr = ''.join(sorted(curr))
            if sorted_curr not in curr_tbl:
                curr_tbl[sorted_curr] = [curr]

            else:
                curr_tbl[sorted_curr].append(curr)
     
        for key in curr_tbl:
            val = curr_tbl[key]
            op.append(val)

        return op