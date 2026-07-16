# LeetCode 0707 - Design Linked List
# https://leetcode.com/problems/design-linked-list/


class _Node:
    def __init__(self, val: int = 0):
        self.val = val
        self.next: _Node | None = None


class MyLinkedList:
    def __init__(self):
        self.dummy = _Node()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        node = self.dummy.next
        for _ in range(index):
            assert node is not None
            node = node.next
        assert node is not None
        return node.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        prev = self.dummy
        for _ in range(index):
            assert prev.next is not None
            prev = prev.next
        node = _Node(val)
        node.next = prev.next
        prev.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        prev = self.dummy
        for _ in range(index):
            assert prev.next is not None
            prev = prev.next
        assert prev.next is not None
        prev.next = prev.next.next
        self.size -= 1
