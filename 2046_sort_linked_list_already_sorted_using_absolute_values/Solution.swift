// LeetCode 2046 - Sort Linked List Already Sorted Using Absolute Values
// https://leetcode.com/problems/sort-linked-list-already-sorted-using-absolute-values/

class ListNode {
    var val: Int
    var next: ListNode?
    init(_ val: Int = 0, _ next: ListNode? = nil) {
        self.val = val
        self.next = next
    }
}

class Solution {
    func sortLinkedList(_ head: ListNode?) -> ListNode? {
        guard let head = head else { return nil }
        var head = head
        var prev = head
        var cur = head.next
        while let node = cur {
            if node.val < 0 {
                prev.next = node.next
                node.next = head
                head = node
                cur = prev.next
            } else {
                prev = node
                cur = node.next
            }
        }
        return head
    }
}
