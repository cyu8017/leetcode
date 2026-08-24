// LeetCode 0876 - Middle of the Linked List
// https://leetcode.com/problems/middle-of-the-linked-list/

class ListNode(var `val`: Int = 0) {
    var next: ListNode? = null
}

class Solution {
    fun middleNode(head: ListNode?): ListNode? {
        var slow = head
        var fast = head
        while (fast != null && fast.next != null) {
            slow = slow!!.next
            fast = fast.next!!.next
        }
        return slow
    }
}
