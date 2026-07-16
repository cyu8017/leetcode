// LeetCode 0431 - Encode N-ary Tree to Binary Tree
// https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/

class Node(var `val`: Int? = null, val children: MutableList<Node> = mutableListOf())

class TreeNode(
    var `val`: Int = 0,
    var left: TreeNode? = null,
    var right: TreeNode? = null,
)

class Solution {
    fun encodeNaryTree(root: Node?): TreeNode? {
        if (root == null) {
            return null
        }
        val binary = TreeNode(root.`val`!!)
        if (root.children.isEmpty()) {
            return binary
        }
        binary.left = encodeNaryTree(root.children[0])
        var sibling = binary.left
        for (i in 1 until root.children.size) {
            sibling!!.right = encodeNaryTree(root.children[i])
            sibling = sibling.right
        }
        return binary
    }

    fun decodeBinaryTree(root: TreeNode?): Node? {
        if (root == null) {
            return null
        }
        val node = Node(root.`val`, mutableListOf())
        var current = root.left
        while (current != null) {
            node.children.add(decodeBinaryTree(current)!!)
            current = current.right
        }
        return node
    }
}
