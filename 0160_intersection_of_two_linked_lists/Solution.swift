// LeetCode 0160 - Intersection of Two Linked Lists
// https://leetcode.com/problems/intersection-of-two-linked-lists/

class ListNode {
    var val: Int
    var next: ListNode?

    init(_ val: Int = 0, _ next: ListNode? = nil) {
        self.val = val
        self.next = next
    }
}

class Solution {
    func getIntersectionNode(_ headA: ListNode?, _ headB: ListNode?) -> ListNode? {
        var a = headA
        var b = headB
        while a !== b {
            a = a?.next ?? headB
            b = b?.next ?? headA
        }
        return a
    }
}