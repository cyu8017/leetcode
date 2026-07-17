// LeetCode 1721 - Swapping Nodes in a Linked List
// https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func swapNodes(_ head: ListNode?, _ k: Int) -> ListNode? {
        var first = head!
        for _ in 0..<(k - 1) {
            first = first.next!
        }
        var fast = first
        var second = head!
        while let next = fast.next {
            fast = next
            second = second.next!
        }
        let temp = first.val
        first.val = second.val
        second.val = temp
        return head
    }
}
