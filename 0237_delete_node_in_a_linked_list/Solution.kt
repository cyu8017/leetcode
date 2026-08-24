// LeetCode 0237 - Delete Node in a Linked List
// https://leetcode.com/problems/delete-node-in-a-linked-list/

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun deleteNode(node: ListNode) {
        node.`val` = node.next!!.`val`
        node.next = node.next!!.next
    }
}
