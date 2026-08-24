// LeetCode 1290 - Convert Binary Number in a Linked List to Integer
// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun getDecimalValue(head: ListNode?): Int {
        var node = head
        var value = 0
        while (node != null) {
            value = value * 2 + node.`val`
            node = node.next
        }
        return value
    }
}
