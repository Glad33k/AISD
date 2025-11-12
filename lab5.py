class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        if self.next is None:
            return str(self.value)
        else:
            return str(self.value) + ' -> '

    def insert_next(self, other) -> None:
        other.next = self.next
        self.next = other

    def remove_next(self) -> None:
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        i = 0
        n = self.head
        while n:
            i += 1
            n = n.next
        return i

    def __str__(self):
        tekst = ""
        n = self.head
        while n:
            if n.next is not None:
                tekst += str(n.value) + " -> "
            else:
                tekst += str(n.value)
            n = n.next
        return tekst

    def push(self, value: Node) -> None:
        if type(value) == Node:
            n = self.head
            self.head = value
            value.next = n
        else:
            value = Node(value)
            n = self.head
            self.head = value
            value.next = n

    def append(self, value) -> None:
        if self.head:
            n = self.head
            while n.next:
                n=n.next
            n.next=Node(value)
        else:
            self.head=Node(value)
    def node(self,at:int)->Node:
        if at>len(self):
            return None

        n=self.head
        for i in range(at):
            n=n.next

        return n
    def pop(self):
        if self.head:
            n=self.head
            self.head=self.head.next
            return n.value
        return None
    def remove(self):
        if self.head:
            if self.head.next is None:
                temp = self.head
                self.head = None
                return temp.value

        n=self.head

        while n.next:
            if n.next.next:
                n = n.next
            else:
                break

        temp = n.next
        n.next = None
        return temp.value






node1 = Node(5)
assert str(node1) == '5'
node0 = Node('Ala', node1)
assert str(node0) == 'Ala -> '
node0.insert_next(Node(2))
assert node0.next.value == 2
node0.remove_next()
assert node0.next == None

list_ = LinkedList()
assert list_.head == None
assert len(list_) == 0

list_.push(1)
list_.push(0)
assert list_.head.value == 0
assert str(list_) == "0 -> 1"

assert len(list_) == 2

list_.append(9)
list_.append(10)
assert str(list_) == "0 -> 1 -> 9 -> 10"
assert len(list_) == 4

assert str(list_.node(at=0)) == "0 -> "
assert str(list_.node(at=1)) == "1 -> "
assert list_.node(at=3).value == 10
assert list_.node(at=3).next is None
assert isinstance(list_.node(at=3), Node)
assert list_.node(at=4) is None
assert list_.node(at=10) is None

first_element = list_.node(at=0)
returned_first_element = list_.pop()
assert first_element.value == returned_first_element
assert str(list_) == "1 -> 9 -> 10"

last_element = list_.node(at=2)
returned_last_element = list_.remove()
assert last_element.value == returned_last_element
assert str(list_) == "1 -> 9"
list_.remove()
assert list_.remove() == 1
assert list_.head is None
assert len(list_) == 0
