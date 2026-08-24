// LeetCode 0968 - Binary Tree Cameras
// https://leetcode.com/problems/binary-tree-cameras/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
    constructor(`val`: Int, left: TreeNode?, right: TreeNode?) : this(`val`) {
        this.left = left
        this.right = right
    }
}

class Solution {
    private var cameras: Int = 0

    fun minCameraCover(root: TreeNode?): Int {
        var rootState = dfs(root)
        return cameras + (if (rootState == 0) 1 else 0)
    }

    // 0 = needs camera, 1 = covered, 2 = has camera
    private fun dfs(node: TreeNode?): Int {
        if (node == null) return 1
        var left = dfs(node.left)
        var right = dfs(node.right)
        if (left == 0 || right == 0) {
            cameras++
            return 2
        }
        if (left == 2 || right == 2) return 1
        return 0
    }
}
