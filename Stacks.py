def push(stack, value):
    stack.append(value)


def pop(stack):
    return stack.pop()


my_stack = []
push(my_stack, 'a')
push(my_stack, 'b')
push(my_stack, 'c')

print(my_stack)

for i in range(3):
    pop(my_stack)
    print(my_stack)

