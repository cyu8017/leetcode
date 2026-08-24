// LeetCode 2807 - Insert Greatest Common Divisors in Linked List
// https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

class ListNode(var `val`: Int = 0) {
    var next: ListNode? = null
}

class Solution {
    fun insertGreatestCommonDivisors(head: ListNode?): ListNode {
        var cur = head
        while (cur != null && cur.next != null) {
            var g = gcd(cur.`val`, cur.next.`val`)
            var node = ListNode(g, cur.next)
            cur.next = node
            cur = node.next
        }
        return head
    }

    private fun gcd(a: Int, b: Int): Int {
        while (b != 0) {
            var t = a % b
            a = b
            b = t
        }
        return a
    }
}
