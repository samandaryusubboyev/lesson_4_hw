class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Error: Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Error: Stack is empty")

    def size(self):
        return len(self.items)

stack = Stack()
stack.push("Alex")
stack.push("Chris")
stack.push("Ronny")
stack.push("Kelly")
stack.push("Alice")
stack.push("Tom")
stack.push("Haland")
stack.push("Morata")
stack.push("Modric")
stack.push("Ramos")
print(f"Ro'yhatda mavjud foydalanuvchilar: {stack.items}")

#POP, PEEK AND SIZE

stack.pop()
stack.peek()
print(f"\nO'chirilgandan keyingi foydalanuvchilar: {stack.items} va ohirida turgan foydalanuvchi: {stack.peek()} va {stack.size()} ta foydalanuchi qoldi")
stack.pop()
stack.peek()
print(f"\nO'chirilgandan keyingi foydalanuvchilar: {stack.items} va ohirida turgan foydalanuvchi: {stack.peek()} va {stack.size()} ta foydalanuchi qoldi")
stack.pop()
stack.peek()
print(f"\nO'chirilgandan keyingi foydalanuvchilar: {stack.items} va ohirida turgan foydalanuvchi: {stack.peek()} va {stack.size()} ta foydalanuchi qoldi")
stack.pop()
stack.peek()
print(f"\nO'chirilgandan keyingi foydalanuvchilar: {stack.items} va ohirida turgan foydalanuvchi: {stack.peek()} va {stack.size()} ta foydalanuchi qoldi")
stack.pop()
stack.peek()
print(f"\nO'chirilgandan keyingi foydalanuvchilar: {stack.items} va ohirida turgan foydalanuvchi: {stack.peek()} va {stack.size()} ta foydalanuchi qoldi")
stack.pop()
stack.peek()
print(f"\nO'chirilgandan keyingi foydalanuvchilar: {stack.items} va ohirida turgan foydalanuvchi: {stack.peek()} va {stack.size()} ta foydalanuchi qoldi")
stack.pop()
stack.peek()
print(f"\nO'chirilgandan keyingi foydalanuvchilar: {stack.items} va ohirida turgan foydalanuvchi: {stack.peek()} va {stack.size()} ta foydalanuchi qoldi")























# Example usage:
# stack = Stack()
#
# stack.push(1)
# stack.push(2)
#  stack.push(3)
#
# print("Stack:", stack.items)
#
# top_item = stack.pop()
# print("Popped:", top_item)
# print("Stack after pop:", stack.items)
#
# peeked_item = stack.peek()
# print("Peeked:", peeked_item)
# print("Stack size:", stack.size())