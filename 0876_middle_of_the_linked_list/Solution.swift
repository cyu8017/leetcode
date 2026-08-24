// LeetCode 0876 - Middle of the Linked List
// https://leetcode.com/problems/middle-of-the-linked-list/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func middleNode(_ head: ListNode?) -> ListNode? {
        var slow = head, fast = head
        while fast != nil && fast?.next != nil {
            slow = slow?.next
            fast = fast?.next?.next
        }
        return slow
    }
}
