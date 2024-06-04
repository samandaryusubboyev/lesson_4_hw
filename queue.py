class Queue:
    def __init__(self):
        self.navbat = []

    def is_empty(self):
        return len(self.navbat) == 0

    def enqueue(self, item):
        self.navbat.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.navbat.pop(0)
        else:
            print("Error: Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.navbat[0]
        else:
            print("Error: Queue is empty")

    def size(self):
        return len(self.navbat)

queue = Queue()
queue.enqueue("Alex")
queue.enqueue("Chris")
queue.enqueue("Ronny")
queue.enqueue("Kelly")
queue.enqueue("Alice")
queue.enqueue("Tom")
queue.enqueue("Haland")
queue.enqueue("Morata")
queue.enqueue("Modric")
queue.enqueue("Ramos")
print(f"Navbatdagi foydalanuvchilar: {queue.navbat}")

queue.dequeue()
queue.peek()
print(f"\nO'chirilgandan keyingi foydalanuvchilar: {queue.navbat} va birinchida turgan foydalanuvchi: {queue.peek()} va {queue.size()} ta foydalanuchi qoldi")
queue.dequeue()
queue.peek()
print(f"\nO'chirilgandan keyingi foydalanuvchilar: {queue.navbat} va birinchida turgan foydalanuvchi: {queue.peek()} va {queue.size()} ta foydalanuchi qoldi")
queue.dequeue()
queue.peek()
print(f"\nO'chirilgandan keyingi foydalanuvchilar: {queue.navbat} va birinchida turgan foydalanuvchi: {queue.peek()} va {queue.size()} ta foydalanuchi qoldi")
queue.dequeue()
queue.peek()
print(f"\nO'chirilgandan keyingi foydalanuvchilar: {queue.navbat} va birinchida turgan foydalanuvchi: {queue.peek()} va {queue.size()} ta foydalanuchi qoldi")
queue.dequeue()
queue.peek()
print(f"\nO'chirilgandan keyingi foydalanuvchilar: {queue.navbat} va birinchida turgan foydalanuvchi: {queue.peek()} va {queue.size()} ta foydalanuchi qoldi")
queue.dequeue()
queue.peek()
print(f"\nO'chirilgandan keyingi foydalanuvchilar: {queue.navbat} va birinchida turgan foydalanuvchi: {queue.peek()} va {queue.size()} ta foydalanuchi qoldi")
