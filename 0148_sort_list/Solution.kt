// LeetCode 0148 - Sort List
// https://leetcode.com/problems/sort-list/

class ListNode(var `val`: Int) { var next: ListNode? = null }
class Solution {
    fun sortList(head: ListNode?): ListNode? {
        if (head?.next == null) return head
        var slow = head; var fast = head; var previous: ListNode? = null
        while (fast?.next != null) { previous = slow; slow = slow!!.next; fast = fast.next!!.next }
        previous!!.next = null
        return merge(sortList(head), sortList(slow))
    }
    private fun merge(left: ListNode?, right: ListNode?): ListNode? {
        val dummy = ListNode(0); var tail = dummy; var first = left; var second = right
        while (first != null && second != null) {
            if (first.`val` <= second.`val`) { tail.next = first; first = first.next } else { tail.next = second; second = second.next }
            tail = tail.next!!
        }
        tail.next = first ?: second
        return dummy.next
    }
}