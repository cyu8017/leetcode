// LeetCode 2674 - Split a Circular Linked List
// https://leetcode.com/problems/split-a-circular-linked-list/

class ListNode(var `val`: Int = 0) {
    var next: ListNode? = null
}

class Solution {
    fun splitCircularLinkedList(list: ListNode?): Array<ListNode?> {
        if (list == null) return arrayOf(null, null)
        var slow = list
        var fast = list
        while (fast!!.next !== list && fast.next!!.next !== list) {
            slow = slow!!.next
            fast = fast.next!!.next
        }
        if (fast.next!!.next === list) fast = fast.next
        val head2 = slow!!.next
        slow.next = list
        fast!!.next = head2
        return arrayOf(list, head2)
    }
}
