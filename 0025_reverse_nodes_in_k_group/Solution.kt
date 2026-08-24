// LeetCode 0025 - Reverse Nodes in k-Group
// https://leetcode.com/problems/reverse-nodes-in-k-group/

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun reverseKGroup(head: ListNode?, k: Int): ListNode? {
        val dummy = ListNode(0)
        dummy.next = head
        var groupPrevious: ListNode? = dummy

        while (true) {
            var kth: ListNode? = groupPrevious
            repeat(k) {
                kth = kth?.next
                if (kth == null) {
                    return dummy.next
                }
            }

            val groupNext = kth!!.next
            var previous: ListNode? = groupNext
            var current = groupPrevious!!.next

            while (current != groupNext) {
                val next = current!!.next
                current.next = previous
                previous = current
                current = next
            }

            val tmp = groupPrevious.next
            groupPrevious.next = kth
            groupPrevious = tmp
        }
    }
}
