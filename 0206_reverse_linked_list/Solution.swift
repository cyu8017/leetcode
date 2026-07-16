// LeetCode 0206 - Reverse Linked List
// https://leetcode.com/problems/reverse-linked-list/

class ListNode {
    var val: Int
    var next: ListNode?

    init(_ val: Int = 0, _ next: ListNode? = nil) {
        self.val = val
        self.next = next
    }
}

class Solution {
    func reverseList(_ head: ListNode?) -> ListNode? {
        var previous: ListNode?
        var current = head
        while let node = current {
            let next = node.next
            node.next = previous
            previous = node
            current = next
        }
        return previous
    }
}