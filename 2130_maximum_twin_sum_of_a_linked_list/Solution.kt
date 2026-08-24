// LeetCode 2130 - Maximum Twin Sum of a Linked List
// https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun pairSum(head: ListNode?): Int {
        var slow = head
        var fast = head
        while (fast != null && fast.next != null) {
            slow = slow!!.next
            fast = fast.next!!.next
        }
        var prev: ListNode? = null
        while (slow != null) {
            val nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        }
        var ans = 0
        var a = head
        var b = prev
        while (b != null) {
            ans = maxOf(ans, a!!.`val` + b.`val`)
            a = a.next
            b = b.next
        }
        return ans
    }
}
