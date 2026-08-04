// LeetCode 1171 - Remove Zero Sum Consecutive Nodes from Linked List
// https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun removeZeroSumSublists(head: ListNode?): ListNode? {
        val dummy = ListNode(0)
        dummy.next = head
        val seen = mutableMapOf<Int, ListNode>()
        var prefix = 0
        var node: ListNode? = dummy
        while (node != null) {
            prefix += node.`val`
            seen[prefix] = node
            node = node.next
        }
        prefix = 0
        node = dummy
        while (node != null) {
            prefix += node.`val`
            node.next = seen[prefix]!!.next
            node = node.next
        }
        return dummy.next
    }
}
