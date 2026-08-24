// LeetCode 2095 - Delete the Middle Node of a Linked List
// https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun deleteMiddle(head: ListNode?): ListNode? {
        if (head?.next == null) return null
        var slow: ListNode? = head
        var fast: ListNode? = head
        var prev: ListNode? = null
        while (fast != null && fast.next != null) {
            prev = slow
            slow = slow!!.next
            fast = fast.next!!.next
        }
        prev!!.next = slow!!.next
        return head
    }
}
