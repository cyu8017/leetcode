// LeetCode 3062 - Winner of the Linked List Game
// https://leetcode.com/problems/winner-of-the-linked-list-game/

class ListNode(var `val`: Int = 0) {
    var next: ListNode? = null
}

class Solution {
    fun gameResult(head: ListNode?): String {
        var node = head
        var odd = 0
        var even = 0
        while (node != null) {
            val a = node.`val`
            val b = node.next!!.`val`
            if (a < b) odd++
            if (a > b) even++
            node = node.next!!.next
        }
        return when {
            odd > even -> "Odd"
            odd < even -> "Even"
            else -> "Tie"
        }
    }
}
