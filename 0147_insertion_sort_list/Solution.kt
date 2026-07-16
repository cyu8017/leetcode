// LeetCode 0147 - Insertion Sort List
// https://leetcode.com/problems/insertion-sort-list/

class ListNode(var `val`: Int) { var next: ListNode? = null }
class Solution {
    fun insertionSortList(head: ListNode?): ListNode? {
        val dummy = ListNode(0)
        var current = head
        while (current != null) {
            var previous = dummy
            while (previous.next != null && previous.next!!.`val` < current.`val`) previous = previous.next!!
            val next = current.next; current.next = previous.next; previous.next = current; current = next
        }
        return dummy.next
    }
}