// LeetCode 0112 - Path Sum
// https://leetcode.com/problems/path-sum/

class Solution {
    fun hasPathSum(root: TreeNode?, targetSum: Int): Boolean {
        if (root == null) return false
        if (root.left == null && root.right == null) return root.`val` == targetSum
        return hasPathSum(root.left, targetSum - root.`val`) ||
            hasPathSum(root.right, targetSum - root.`val`)
    }
}

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}