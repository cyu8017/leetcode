// LeetCode 0061 - Rotate List
// https://leetcode.com/problems/rotate-list/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func rotateRight(_ head: ListNode?, _ k: Int) -> ListNode? {
        guard let head = head, head.next != nil else {
            return head
        }

        var tail: ListNode = head
        var length = 1
        while let next = tail.next {
            tail = next
            length += 1
        }

        tail.next = head
        let remaining = k % length
        if remaining == 0 {
            tail.next = nil
            return head
        }

        let steps = length - remaining
        var newTail: ListNode = head
        for _ in 0..<(steps - 1) {
            newTail = newTail.next!
        }

        let newHead = newTail.next
        newTail.next = nil
        return newHead
    }
}
