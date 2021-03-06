class Solution:
    # my solution
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        n = sum(A) // 3
        
        cnt, rest = 0, n
        for i in range(len(A)):
            rest -= A[i]
            if rest == 0:
                cnt += 1
                rest = n
                
        return cnt >= 3: