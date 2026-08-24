// LeetCode 0707 - Design Linked List
// https://leetcode.com/problems/design-linked-list/

class MyLinkedList {
    private class Node {
        var val: Int
        var next: Node?
        init(_ val: Int) { self.val = val }
    }
    private var head: Node?
    private var size = 0

    init() {}

    func get(_ index: Int) -> Int {
        guard index >= 0, index < size else { return -1 }
        var cur = head
        for _ in 0..<index { cur = cur?.next }
        return cur!.val
    }

    func addAtHead(_ val: Int) {
        let node = Node(val)
        node.next = head
        head = node
        size += 1
    }

    func addAtTail(_ val: Int) {
        if size == 0 { addAtHead(val); return }
        var cur = head
        while cur?.next != nil { cur = cur?.next }
        cur?.next = Node(val)
        size += 1
    }

    func addAtIndex(_ index: Int, _ val: Int) {
        if index < 0 || index > size { return }
        if index == 0 { addAtHead(val); return }
        var cur = head
        for _ in 0..<(index - 1) { cur = cur?.next }
        let node = Node(val)
        node.next = cur?.next
        cur?.next = node
        size += 1
    }

    func deleteAtIndex(_ index: Int) {
        if index < 0 || index >= size { return }
        if index == 0 { head = head?.next; size -= 1; return }
        var cur = head
        for _ in 0..<(index - 1) { cur = cur?.next }
        cur?.next = cur?.next?.next
        size -= 1
    }
}
