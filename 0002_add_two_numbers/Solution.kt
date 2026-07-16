// LeetCode 0002 - Add Two Numbers
// https://leetcode.com/problems/add-two-numbers/

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        val dummy = ListNode(0)
        var current: ListNode? = dummy
        var carry = 0
        var node1 = l1
        var node2 = l2

        while (node1 != null || node2 != null || carry != 0) {
            var total = carry
            if (node1 != null) {
                total += node1!!.`val`
                node1 = node1.next
            }
            if (node2 != null) {
                total += node2!!.`val`
                node2 = node2.next
            }
            carry = total / 10
            current!!.next = ListNode(total % 10)
            current = current.next
        }

        return dummy.next
    }
}
