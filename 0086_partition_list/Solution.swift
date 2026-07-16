// LeetCode 0086 - Partition List
// https://leetcode.com/problems/partition-list/

class ListNode {
    var val: Int
    var next: ListNode?
    init() { val = 0; next = nil }
    init(_ val: Int) { self.val = val; next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

class Solution {
    func partition(_ head: ListNode?, _ x: Int) -> ListNode? {
        let beforeHead = ListNode(0)
        let afterHead = ListNode(0)
        var before = beforeHead
        var after = afterHead
        var current = head

        while let node = current {
            if node.val < x {
                before.next = node
                before = before.next!
            } else {
                after.next = node
                after = after.next!
            }
            current = node.next
        }

        after.next = nil
        before.next = afterHead.next
        return beforeHead.next
    }
}
