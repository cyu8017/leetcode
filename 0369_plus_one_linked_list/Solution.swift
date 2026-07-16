// LeetCode 0369 - Plus One Linked List
// https://leetcode.com/problems/plus-one-linked-list/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { self.val = 0; self.next = nil }
    init(_ val: Int) { self.val = val; self.next = nil }
    init(_ val: Int, _ next: ListNode?) {
        self.val = val
        self.next = next
    }
}

class Solution {
    func plusOne(_ head: ListNode?) -> ListNode? {
        let sentinel = ListNode(0, head)
        var notNine: ListNode = sentinel
        var node = head

        while let current = node {
            if current.val != 9 {
                notNine = current
            }
            node = current.next
        }

        notNine.val += 1
        node = notNine.next
        while let current = node {
            current.val = 0
            node = current.next
        }

        return sentinel.val == 1 ? sentinel : sentinel.next
    }
}
