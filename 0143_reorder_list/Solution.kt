// LeetCode 0143 - Reorder List
// https://leetcode.com/problems/reorder-list/

class ListNode(var `val`: Int) { var next: ListNode? = null }
class Solution {
    fun reorderList(head: ListNode?) {
        if (head?.next == null) return
        var slow = head; var fast = head
        while (fast?.next?.next != null) { slow = slow!!.next; fast = fast.next!!.next }
        var second = slow!!.next; slow.next = null; var previous: ListNode? = null
        while (second != null) { val next = second.next; second.next = previous; previous = second; second = next }
        var first = head; second = previous
        while (second != null) {
            val firstNext = first!!.next; val secondNext = second.next
            first.next = second; second.next = firstNext; first = firstNext; second = secondNext
        }
    }
}