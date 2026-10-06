class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        balance = 0
        answer = 0
        for ch in s:
            
            if ch == '(':
                balance += 1
            elif balance  > 0:
                balance -= 1
            else:
                answer  += 1
        return balance + answer


        
        