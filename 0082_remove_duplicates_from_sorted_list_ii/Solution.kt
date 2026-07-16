// LeetCode 0082 - Remove Duplicates from Sorted List II
// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun deleteDuplicates(head: ListNode?): ListNode? {
        val dummy = ListNode(0)
        dummy.next = head
        var previous: ListNode? = dummy
        var current = head

        while (current != null) {
            if (current.next != null && current.`val` == current.next!!.`val`) {
                while (current!!.next != null && current.`val` == current.next!!.`val`) {
                    current = current.next
                }
                previous!!.next = current!!.next
            } else {
                previous = previous!!.next
            }
            current = current!!.next
        }

        return dummy.next
    }
}
