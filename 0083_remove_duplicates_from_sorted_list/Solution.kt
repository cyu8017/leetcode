// LeetCode 0083 - Remove Duplicates from Sorted List
// https://leetcode.com/problems/remove-duplicates-from-sorted-list/

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun deleteDuplicates(head: ListNode?): ListNode? {
        var current = head

        while (current != null && current.next != null) {
            if (current.`val` == current.next!!.`val`) {
                current.next = current.next!!.next
            } else {
                current = current.next
            }
        }

        return head
    }
}
