class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        score = 0

        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
                score += stack[-1]
            elif op == 'D':
                stack.append(stack[-1] * 2)
                score += stack[-1]
            elif op == 'C':
                score -= stack.pop()
            else:
                stack.append(int(op))
                score += stack[-1]
                
        return score