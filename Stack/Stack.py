stack = []

stack.append('https://www.cnn.com/')
stack.append('https://www.cnn.com/world')
stack.append('https://www.cnn.com/india')
stack.append('https://www.cnn.com/china')

print(stack)

print(stack.pop())
# 'https://www.cnn.com/china'
print(stack.pop())
# 'https://www.cnn.com/india'
print(stack.pop())

print(stack[-1])