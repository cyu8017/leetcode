// LeetCode 0430 - Flatten a Multilevel Doubly Linked List
// https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

class Node(
    var `val`: Int = 0,
    var prev: Node? = null,
    var next: Node? = null,
    var child: Node? = null,
)

class Solution {
    fun flatten(head: Node?): Node? {
        var current = head
        while (current != null) {
            if (current.child != null) {
                val nextNode = current.next
                val childHead = flatten(current.child)
                current.next = childHead
                childHead!!.prev = current
                var tail = childHead
                while (tail.next != null) {
                    tail = tail.next!!
                }
                tail.next = nextNode
                if (nextNode != null) {
                    nextNode.prev = tail
                }
                current.child = null
            }
            current = current.next
        }
        return head
    }
}
