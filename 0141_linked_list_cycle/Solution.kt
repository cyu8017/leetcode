// LeetCode 0141 - Linked List Cycle
// https://leetcode.com/problems/linked-list-cycle/

class ListNode(var `val`: Int) { var next: ListNode? = null }
class Solution {
    fun hasCycle(head: ListNode?): Boolean {
        var slow = head; var fast = head
        while (fast?.next != null) {
            slow = slow!!.next; fast = fast.next!!.next
            if (slow === fast) return true
        }
        return false
    }
}