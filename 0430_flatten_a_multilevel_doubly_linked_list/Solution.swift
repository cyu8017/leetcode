// LeetCode 0430 - Flatten a Multilevel Doubly Linked List
// https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

class Node {
    var val: Int
    var prev: Node?
    var next: Node?
    var child: Node?

    init(_ val: Int, _ prev: Node? = nil, _ next: Node? = nil, _ child: Node? = nil) {
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
    }
}

class Solution {
    func flatten(_ head: Node?) -> Node? {
        var current = head
        while let node = current {
            if let child = node.child {
                let nextNode = node.next
                let childHead = flatten(child)
                node.next = childHead
                childHead?.prev = node
                var tail = childHead
                while tail?.next != nil {
                    tail = tail?.next
                }
                tail?.next = nextNode
                nextNode?.prev = tail
                node.child = nil
            }
            current = node.next
        }
        return head
    }
}
