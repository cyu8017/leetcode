// LeetCode 0725 - Split Linked List in Parts
// https://leetcode.com/problems/split-linked-list-in-parts/

class ListNode(var `val`: Int = 0) {
    var next: ListNode? = null
}

class Solution {
    fun splitListToParts(head: ListNode?, k: Int): Array<ListNode?> {
        var length = 0
        var node = head
        while (node != null) {
            length++
            node = node.next
        }
        val partSize = length / k
        val extra = length % k
        val result = arrayOfNulls<ListNode>(k)
        var current = head
        for (i in 0 until k) {
            result[i] = current
            val size = partSize + if (i < extra) 1 else 0
            var j = 0
            while (j < size - 1 && current != null) {
                current = current.next
                j++
            }
            if (current != null) {
                val nxt = current.next
                current.next = null
                current = nxt
            }
        }
        return result
    }
}
