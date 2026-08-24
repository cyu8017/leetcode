// LeetCode 0092 - Reverse Linked List II
// https://leetcode.com/problems/reverse-linked-list-ii/

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun reverseBetween(head: ListNode?, left: Int, right: Int): ListNode? {
        if (head == null || left == right) {
            return head
        }

        val dummy = ListNode(0)
        dummy.next = head
        var before = dummy
        repeat(left - 1) {
            before = before.next!!
        }

        val start = before.next!!
        var current = start.next

        repeat(right - left) {
            start.next = current!!.next
            current.next = before.next
            before.next = current
            current = start.next
        }

        return dummy.next
    }
}
