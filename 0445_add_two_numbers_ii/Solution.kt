// LeetCode 0445 - Add Two Numbers II
// https://leetcode.com/problems/add-two-numbers-ii/

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        val stack1 = ArrayDeque<Int>()
        val stack2 = ArrayDeque<Int>()
        var node1 = l1
        var node2 = l2
        while (node1 != null) {
            stack1.addLast(node1.`val`)
            node1 = node1.next
        }
        while (node2 != null) {
            stack2.addLast(node2.`val`)
            node2 = node2.next
        }

        var carry = 0
        var head: ListNode? = null
        while (stack1.isNotEmpty() || stack2.isNotEmpty() || carry != 0) {
            var total = carry
            if (stack1.isNotEmpty()) {
                total += stack1.removeLast()
            }
            if (stack2.isNotEmpty()) {
                total += stack2.removeLast()
            }
            carry = total / 10
            head = ListNode(total % 10).also { it.next = head }
        }
        return head
    }
}
