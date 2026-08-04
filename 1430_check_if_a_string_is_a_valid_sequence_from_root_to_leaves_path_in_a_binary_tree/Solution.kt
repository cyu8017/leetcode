// LeetCode 1430 - Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
// https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun isValidSequence(root: TreeNode?, arr: IntArray): Boolean {
        fun visit(node: TreeNode?, index: Int): Boolean {
            if (node == null || index == arr.size || node.`val` != arr[index]) return false
            if (node.left == null && node.right == null) return index == arr.size - 1
            return visit(node.left, index + 1) || visit(node.right, index + 1)
        }
        return visit(root, 0)
    }
}
