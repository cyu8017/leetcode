// LeetCode 1836 - Remove Duplicates From an Unsorted Linked List
// https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/

class ListNode(var `val`: Int = 0, var next: ListNode? = null)

class Solution {
    fun deleteDuplicatesUnsorted(head: ListNode?): ListNode? {
        val counts = HashMap<Int, Int>()
        var node = head
        while (node != null) {
            counts[node.`val`] = (counts[node.`val`] ?: 0) + 1
            node = node.next
        }
        val dummy = ListNode(0, head)
        var prev = dummy
        node = head
        while (node != null) {
            if ((counts[node.`val`] ?: 0) > 1) {
                prev.next = node.next
                node = node.next
            } else {
                prev = node
                node = node.next
            }
        }
        return dummy.next
    }
}
