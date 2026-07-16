// LeetCode 0235 - Lowest Common Ancestor of a Binary Search Tree
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

class TreeNode(var `val`: Int = 0, var left: TreeNode? = null, var right: TreeNode? = null)

class Solution {
    fun lowestCommonAncestor(root: TreeNode?, p: TreeNode, q: TreeNode): TreeNode? {
        var current = root
        while (current != null) {
            when {
                p.`val` < current.`val` && q.`val` < current.`val` -> current = current.left
                p.`val` > current.`val` && q.`val` > current.`val` -> current = current.right
                else -> return current
            }
        }
        return current
    }
}
