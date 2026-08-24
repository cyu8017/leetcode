// LeetCode 0021 - Merge Two Sorted Lists
// https://leetcode.com/problems/merge-two-sorted-lists/

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun mergeTwoLists(list1: ListNode?, list2: ListNode?): ListNode? {
        val dummy = ListNode(0)
        var current: ListNode? = dummy
        var node1 = list1
        var node2 = list2

        while (node1 != null && node2 != null) {
            if (node1.`val` <= node2.`val`) {
                current!!.next = node1
                node1 = node1.next
            } else {
                current!!.next = node2
                node2 = node2.next
            }
            current = current.next
        }

        current!!.next = node1 ?: node2
        return dummy.next
    }
}
