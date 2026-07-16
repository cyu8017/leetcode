// LeetCode 0117 - Populating Next Right Pointers in Each Node II
// https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

import java.util.ArrayDeque

class Node(var `val`: Int = 0) {
    var left: Node? = null
    var right: Node? = null
    var next: Node? = null
}

class Solution {
    fun connect(root: Node?): Node? {
        if (root == null) return null
        val queue = ArrayDeque<Node>()
        queue.add(root)
        while (queue.isNotEmpty()) {
            var previous: Node? = null
            repeat(queue.size) {
                val node = queue.removeFirst()
                previous?.next = node
                previous = node
                node.left?.let(queue::addLast)
                node.right?.let(queue::addLast)
            }
            previous?.next = null
        }
        return root
    }
}