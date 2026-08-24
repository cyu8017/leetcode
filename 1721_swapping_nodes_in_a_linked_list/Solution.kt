// LeetCode 1721 - Swapping Nodes in a Linked List
// https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun swapNodes(head: ListNode?, k: Int): ListNode? {
        var first = head!!
        repeat(k - 1) {
            first = first.next!!
        }
        var fast = first
        var second = head
        while (fast.next != null) {
            fast = fast.next!!
            second = second!!.next
        }
        val temp = first.`val`
        first.`val` = second!!.`val`
        second.`val` = temp
        return head
    }
}
