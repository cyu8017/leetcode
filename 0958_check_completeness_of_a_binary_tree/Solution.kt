// LeetCode 0958 - Check Completeness of a Binary Tree
// https://leetcode.com/problems/check-completeness-of-a-binary-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
    constructor(`val`: Int, left: TreeNode?, right: TreeNode?) : this(`val`) {
        this.left = left
        this.right = right
    }
}

class Solution {
    fun isCompleteTree(root: TreeNode?): Boolean {
        var q = ArrayDeque()
        q.add(root)
        var end = false
        while (!q.isEmpty()) {
            var node = q.removeFirst()
            if (node == null) end = true
            else {
                if (end) return false
                q.add(node.left)
                q.add(node.right)
            }
        }
        return true
    }
}
