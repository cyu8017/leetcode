// LeetCode 0708 - Insert into a Sorted Circular Linked List
// https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

class Node {
    var val: Int
    var next: Node?
    init(_ val: Int) { self.val = val }
    init(_ val: Int, _ next: Node?) { self.val = val; self.next = next }
}

class Solution {
    func insert(_ head: Node?, _ insertVal: Int) -> Node? {
        let node = Node(insertVal)
        guard let head else {
            node.next = node
            return node
        }
        var cur = head
        while cur.next !== head { cur = cur.next! }
        cur.next = head
        var prev = head
        var curr = head.next!
        while true {
            if prev.val <= insertVal && insertVal <= curr.val { break }
            if prev.val > curr.val && (insertVal >= prev.val || insertVal <= curr.val) { break }
            prev = curr
            curr = curr.next!
            if prev === head { break }
        }
        prev.next = node
        node.next = curr
        return head
    }
}
