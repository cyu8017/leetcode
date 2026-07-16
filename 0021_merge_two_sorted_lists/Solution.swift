// LeetCode 0021 - Merge Two Sorted Lists
// https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func mergeTwoLists(_ list1: ListNode?, _ list2: ListNode?) -> ListNode? {
        let dummy = ListNode()
        var current: ListNode? = dummy
        var node1 = list1
        var node2 = list2

        while let n1 = node1, let n2 = node2 {
            if n1.val <= n2.val {
                current?.next = n1
                node1 = n1.next
            } else {
                current?.next = n2
                node2 = n2.next
            }
            current = current?.next
        }

        current?.next = node1 ?? node2
        return dummy.next
    }
}
