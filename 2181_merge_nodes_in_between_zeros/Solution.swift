// LeetCode 2181 - Merge Nodes in Between Zeros
// https://leetcode.com/problems/merge-nodes-in-between-zeros/

class ListNode {
    var val: Int
    var next: ListNode?
    init(_ val: Int = 0, _ next: ListNode? = nil) {
        self.val = val
        self.next = next
    }
}

class Solution {
    func mergeNodes(_ head: ListNode?) -> ListNode? {
        let dummy = ListNode()
        var cur: ListNode? = dummy
        var sum = 0
        var p = head?.next
        while let node = p {
            if node.val == 0 {
                cur?.next = ListNode(sum)
                cur = cur?.next
                sum = 0
            } else {
                sum += node.val
            }
            p = node.next
        }
        return dummy.next
    }
}
