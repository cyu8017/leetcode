// LeetCode 2487 - Remove Nodes From Linked List
// https://leetcode.com/problems/remove-nodes-from-linked-list/

class ListNode(var `val`: Int) {
    var next: ListNode? = null
}

class Solution {
    fun removeNodes(head: ListNode): ListNode {
            head = Rev(head)
            var mx: Int = 0
            var dummy: ListNode = ListNode(0, head)
            var prev: ListNode = dummy
            while (prev.next != null) {
                if (prev.next.val >= mx) {
                    mx = prev.next.val
                    prev = prev.next
                } else {
                    prev.next = prev.next.next
                }
            }
            return rev(dummy.next)
    }
    private fun rev(node: ListNode): ListNode {
            var prev: ListNode = null
            while (node != null) {
                var nxt: ListNode = node.next
                node.next = prev
                prev = node
                node = nxt
            }
            return prev
    }
}
