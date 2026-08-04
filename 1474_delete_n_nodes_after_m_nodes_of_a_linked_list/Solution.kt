// LeetCode 1474 - Delete N Nodes After M Nodes of a Linked List
// https://leetcode.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun deleteNodes(head: ListNode?, m: Int, n: Int): ListNode? {
        var cur = head
        while (cur != null) {
            repeat(m - 1) {
                if (cur == null) return@repeat
                cur = cur!!.next
            }
            if (cur == null) break
            var drop = cur!!.next
            repeat(n) {
                if (drop != null) drop = drop!!.next
            }
            cur!!.next = drop
            cur = drop
        }
        return head
    }
}
