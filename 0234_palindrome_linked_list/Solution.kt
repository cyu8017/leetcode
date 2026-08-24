// LeetCode 0234 - Palindrome Linked List
// https://leetcode.com/problems/palindrome-linked-list/

class ListNode(var `val`: Int = 0, var next: ListNode? = null)

class Solution {
    fun isPalindrome(head: ListNode?): Boolean {
        if (head?.next == null) {
            return true
        }

        var slow: ListNode? = head
        var fast: ListNode? = head
        while (fast?.next != null) {
            slow = slow?.next
            fast = fast.next?.next
        }

        var prev: ListNode? = null
        var current = slow
        while (current != null) {
            val next = current.next
            current.next = prev
            prev = current
            current = next
        }

        var left: ListNode? = head
        var right = prev
        while (right != null) {
            if (left?.`val` != right.`val`) {
                return false
            }
            left = left?.next
            right = right.next
        }
        return true
    }
}
