// LeetCode 0237 - Delete Node in a Linked List
// https://leetcode.com/problems/delete-node-in-a-linked-list/

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
    func deleteNode(_ node: ListNode) {
        node.val = node.next!.val
        node.next = node.next!.next
    }
}
