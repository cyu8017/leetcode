// LeetCode 0206 - Reverse Linked List\n// https://leetcode.com/problems/\n\nclass ListNode(var `val`: Int = 0, var next: ListNode? = null)

class Solution {
    fun reverseList(head: ListNode?): ListNode? {
        var current = head; var previous: ListNode? = null
        while (current != null) { val next = current.next; current.next = previous; previous = current; current = next }
        return previous
    }
}
