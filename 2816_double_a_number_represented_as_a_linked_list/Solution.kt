// LeetCode 2816 - Double a Number Represented as a Linked List
// https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

class ListNode(var `val`: Int = 0) {
    var next: ListNode? = null
}

class Solution {
    fun doubleIt(head: ListNode?): ListNode {
        head = rev(head)
        var carry = 0
        var cur = head
        var prev = null
        while (cur != null) {
            var `val` = cur.`val` * 2 + carry
            cur.`val` = val % 10
            carry = val / 10
            prev = cur
            cur = cur.next
        }
        if (carry > 0) prev.next = ListNode(carry)
        return rev(head)
    }

    private fun rev(node: ListNode?): ListNode {
        var prev = null
        while (node != null) {
            var nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        }
        return prev
    }
}
