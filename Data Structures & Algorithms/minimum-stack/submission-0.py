class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack or val <=self.minstack[-1]:
            self.minstack.append(val)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self) -> None:
        if not self.minstack:
            return
        self.minstack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        if not self.stack:
            return -1
        return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.minstack:
            return -1
        return self.minstack[-1]
        
