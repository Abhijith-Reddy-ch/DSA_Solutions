class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            if tokens[i] not in ["+","-","/","*"]:
                stack.append(int(tokens[i]))
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if tokens[i] == '/':
                    ans = int(num1/num2)
                else:
                    ans = eval(f"{num1}{tokens[i]}{num2}") 
                stack.append(ans)
        
        return stack.pop()