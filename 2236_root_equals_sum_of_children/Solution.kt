// LeetCode 2236 - Root Equals Sum of Children
// https://leetcode.com/problems/root-equals-sum-of-children/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
    constructor(`val`: Int, left: TreeNode?, right: TreeNode?) : this(`val`) {
        this.left = left
        this.right = right
    }
}

class Solution {
    fun checkTree(root: TreeNode): Boolean {
        return root.`val` == root.left!!.`val` + root.right!!.`val`
    }
}
