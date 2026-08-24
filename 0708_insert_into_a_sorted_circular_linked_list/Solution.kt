// LeetCode 0708 - Insert into a Sorted Circular Linked List
// https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

class Node(var `val`: Int = 0) {
    var next: Node? = null
}

class Solution {
    fun insert(head: Node?, insertVal: Int): Node? {
        val node = Node(insertVal)
        if (head == null) {
            node.next = node
            return node
        }
        var cur = head
        while (cur!!.next != null && cur.next !== head) cur = cur.next
        cur.next = head
        var prev = head
        var curr = head.next
        while (true) {
            if (prev.`val` <= insertVal && insertVal <= curr!!.`val`) break
            if (prev.`val` > curr.`val` && (insertVal >= prev.`val` || insertVal <= curr.`val`)) break
            prev = curr
            curr = curr.next
            if (prev === head) break
        }
        prev.next = node
        node.next = curr
        return head
    }
}
