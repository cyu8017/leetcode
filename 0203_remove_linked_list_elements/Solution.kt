// LeetCode 0203 - Remove Linked List Elements\n// https://leetcode.com/problems/\n\nclass ListNode(var `val`: Int = 0, var next: ListNode? = null)

class Solution {
    fun removeElements(head: ListNode?, `val`: Int): ListNode? {
        val dummy = ListNode(0, head); var current = dummy
        while (current.next != null) {
            if (current.next!!.`val` == `val`) current.next = current.next!!.next else current = current.next!!
        }
        return dummy.next
    }
}
