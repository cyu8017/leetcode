// LeetCode 0429 - N-ary Tree Level Order Traversal
// https://leetcode.com/problems/n-ary-tree-level-order-traversal/

class Node(var `val`: Int? = null, val children: MutableList<Node> = mutableListOf())

class Solution {
    fun levelOrder(root: Node?): List<List<Int>> {
        if (root == null) {
            return emptyList()
        }

        val result = mutableListOf<List<Int>>()
        val queue = ArrayDeque<Node>()
        queue.add(root)

        while (queue.isNotEmpty()) {
            val level = mutableListOf<Int>()
            repeat(queue.size) {
                val node = queue.removeFirst()
                level.add(node.`val`!!)
                queue.addAll(node.children)
            }
            result.add(level)
        }

        return result
    }
}
