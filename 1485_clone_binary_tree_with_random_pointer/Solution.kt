// LeetCode 1485 - Clone Binary Tree With Random Pointer
// https://leetcode.com/problems/clone-binary-tree-with-random-pointer/

class Node(var `val`: Int) {
    var left: Node? = null
    var right: Node? = null
    var random: Node? = null
}

class Solution {
    private val copies = HashMap<Node, Node>()

    fun copyRandomBinaryTree(root: Node?): Node? {
        if (root == null) return null
        copies[root]?.let { return it }
        val copy = Node(root.`val`)
        copies[root] = copy
        copy.left = copyRandomBinaryTree(root.left)
        copy.right = copyRandomBinaryTree(root.right)
        copy.random = copyRandomBinaryTree(root.random)
        return copy
    }
}
