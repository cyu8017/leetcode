// LeetCode 0092 - Reverse Linked List II
// https://leetcode.com/problems/reverse-linked-list-ii/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func reverseBetween(_ head: ListNode?, _ left: Int, _ right: Int) -> ListNode? {
        if head == nil || left == right {
            return head
        }

        let dummy = ListNode(0, head)
        var before = dummy
        for _ in 0..<(left - 1) {
            before = before.next!
        }

        let start = before.next!
        var current = start.next

        for _ in 0..<(right - left) {
            start.next = current!.next
            current!.next = before.next
            before.next = current
            current = start.next
        }

        return dummy.next
    }
}
