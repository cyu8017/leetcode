// LeetCode 2095 - Delete the Middle Node of a Linked List
// https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

class ListNode {
    var val: Int
    var next: ListNode?
    init(_ val: Int = 0, _ next: ListNode? = nil) {
        self.val = val
        self.next = next
    }
}

class Solution {
    func deleteMiddle(_ head: ListNode?) -> ListNode? {
        guard head?.next != nil else { return nil }
        var slow = head, fast = head, prev: ListNode?
        while fast != nil && fast?.next != nil {
            prev = slow
            slow = slow?.next
            fast = fast?.next?.next
        }
        prev?.next = slow?.next
        return head
    }
}
