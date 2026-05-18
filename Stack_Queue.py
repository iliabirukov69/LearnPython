class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pull(self):
        if self.is_empty():
            raise IndexError("Попытка взять элемент из пустого стека")
        removed_data = self.top.data
        self.top = self.top.next
        return removed_data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def display(self):
        current = self.top
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Стек (top -> bottom):", " -> ".join(elements) if elements else "Стек пуст")


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data


if __name__ == "__main__":
    my_stack = Stack()
    print(f"Стек пустой? {my_stack.is_empty()}")

    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)
    my_stack.display()

    print(f"\nЧто сейчас на вершине (peek)? {my_stack.peek()}")

    popped = my_stack.pull()
    print(f"Мы забрали из стека: {popped}")
    my_stack.display()

    print(f"Мы забрали из стека: {my_stack.pull()}")
    my_stack.display()
