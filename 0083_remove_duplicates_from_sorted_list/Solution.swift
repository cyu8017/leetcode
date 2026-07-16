// LeetCode 0083 - Remove Duplicates from Sorted List
// https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func deleteDuplicates(_ head: ListNode?) -> ListNode? {
        var current = head

        while let node = current, let next = node.next {
            if node.val == next.val {
                node.next = next.next
            } else {
                current = node.next
            }
        }

        return head
    }
}
