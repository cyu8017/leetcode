// LeetCode 0142 - Linked List Cycle II
// https://leetcode.com/problems/linked-list-cycle-ii/

class ListNode(var `val`: Int) { var next: ListNode? = null }
class Solution {
    fun detectCycle(head: ListNode?): ListNode? {
        var slow = head; var fast = head
        while (fast?.next != null) {
            slow = slow!!.next; fast = fast.next!!.next
            if (slow === fast) {
                slow = head
                while (slow !== fast) { slow = slow!!.next; fast = fast!!.next }
                return slow
            }
        }
        return null
    }
}