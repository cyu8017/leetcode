// LeetCode 2181 - Merge Nodes in Between Zeros
// https://leetcode.com/problems/merge-nodes-in-between-zeros/

class ListNode(var `val`: Int = 0) {
    var next: ListNode? = null
}

class Solution {
    fun mergeNodes(head: ListNode?): ListNode? {
        val dummy = ListNode()
        var cur = dummy
        var sum = 0
        var p = head!!.next
        while (p != null) {
            if (p.`val` == 0) {
                cur.next = ListNode(sum)
                cur = cur.next!!
                sum = 0
            } else {
                sum += p.`val`
            }
            p = p.next
        }
        return dummy.next
    }
}
