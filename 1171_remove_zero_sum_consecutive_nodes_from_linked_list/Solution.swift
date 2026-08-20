class ListNode {
    var val: Int
    var next: ListNode?
    init() { self.val = 0; self.next = nil }
    init(_ val: Int) { self.val = val; self.next = nil }
    init(_ val: Int, _ next: ListNode?) { self.val = val; self.next = next }
}

// LeetCode 1171 - Remove Zero Sum Consecutive Nodes from Linked List
// https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

class Solution {
    func removeZeroSumSublists(_ head: ListNode?) -> ListNode? {
        let dummy = ListNode(0)
        dummy.next = head
        var prefix = 0
        var seen: [Int: ListNode] = [:]
        var node: ListNode? = dummy
        while let cur = node {
            prefix += cur.val
            seen[prefix] = cur
            node = cur.next
        }
        prefix = 0
        node = dummy
        while let cur = node {
            prefix += cur.val
            cur.next = seen[prefix]!.next
            node = cur.next
        }
        return dummy.next
    }
}
