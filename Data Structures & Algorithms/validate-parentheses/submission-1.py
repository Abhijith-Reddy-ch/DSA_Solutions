class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            if s[i] in ["(","{","["]:
                stack.append(s[i])
            else:
                if not stack:
                    return False

                top = stack.pop()

                if s[i] == ")" and top == "(":
                    continue
                if s[i] == "}" and top == "{":
                    continue
                if s[i] == "]" and top == "[":
                    continue

                return False
        
        return not stack
