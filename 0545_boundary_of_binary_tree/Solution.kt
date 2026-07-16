// LeetCode 0545 - Boundary of Binary Tree
// https://leetcode.com/problems/boundary-of-binary-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun boundaryOfBinaryTree(root: TreeNode?): List<Int> {
        if (root == null) {
            return emptyList()
        }
        if (isLeaf(root)) {
            return listOf(root.`val`)
        }

        return buildList {
            add(root.`val`)
            addAll(leftBoundary(root.left))
            addAll(leaves(root))
            addAll(rightBoundary(root.right))
        }
    }

    private fun isLeaf(node: TreeNode?): Boolean {
        return node != null && node.left == null && node.right == null
    }

    private fun leftBoundary(node: TreeNode?): List<Int> {
        if (node == null || isLeaf(node)) {
            return emptyList()
        }
        return buildList {
            add(node.`val`)
            if (node.left != null) {
                addAll(leftBoundary(node.left))
            } else {
                addAll(leftBoundary(node.right))
            }
        }
    }

    private fun rightBoundary(node: TreeNode?): List<Int> {
        if (node == null || isLeaf(node)) {
            return emptyList()
        }
        return buildList {
            if (node.right != null) {
                addAll(rightBoundary(node.right))
            } else {
                addAll(rightBoundary(node.left))
            }
            add(node.`val`)
        }
    }

    private fun leaves(node: TreeNode?): List<Int> {
        if (node == null) {
            return emptyList()
        }
        if (isLeaf(node)) {
            return listOf(node.`val`)
        }
        return leaves(node.left) + leaves(node.right)
    }
}
