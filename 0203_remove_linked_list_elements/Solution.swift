// LeetCode 0203 - Remove Linked List Elements
// https://leetcode.com/problems/remove-linked-list-elements/

class ListNode {
    var val: Int
    var next: ListNode?

    init(_ val: Int = 0, _ next: ListNode? = nil) {
        self.val = val
        self.next = next
    }
}

class Solution {
    func removeElements(_ head: ListNode?, _ val: Int) -> ListNode? {
        let dummy = ListNode(0, head)
        var current: ListNode? = dummy
        while let next = current?.next {
            if next.val == val {
                current?.next = next.next
            } else {
                current = next
            }
        }
        return dummy.next
    }
}