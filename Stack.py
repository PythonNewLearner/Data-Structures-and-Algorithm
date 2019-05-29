class Stack:
    def __init__(self):
        self.stack=[]

    def isEmpty(self):
        return self.stack==[]

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        data=self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    def sizeStack(self):
        return len(self.stack)

stak=Stack()
stak.push(1)
stak.push(2)
stak.push(3)
print("stack size :",stak.sizeStack())
print('Popped: ', stak.pop())
print('stack size: ',stak.sizeStack())
print("Peek: ", stak.peek())
print('stack size: ',stak.sizeStack())