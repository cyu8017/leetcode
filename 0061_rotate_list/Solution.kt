// LeetCode 0061 - Rotate List
// https://leetcode.com/problems/rotate-list/

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun rotateRight(head: ListNode?, k: Int): ListNode? {
        if (head?.next == null) {
            return head
        }

        var tail = head
        var length = 1
        while (tail?.next != null) {
            tail = tail.next
            length++
        }

        tail?.next = head
        var remaining = k % length
        if (remaining == 0) {
            tail?.next = null
            return head
        }

        val steps = length - remaining
        var newTail = head
        repeat(steps - 1) {
            newTail = newTail?.next
        }

        val newHead = newTail?.next
        newTail?.next = null
        return newHead
    }
}
