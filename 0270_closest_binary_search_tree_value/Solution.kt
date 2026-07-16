// LeetCode 0270 - Closest Binary Search Tree Value
// https://leetcode.com/problems/closest-binary-search-tree-value/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun closestValue(root: TreeNode?, target: Double): Int {
        var closest = root!!.`val`
        var current: TreeNode? = root
        while (current != null) {
            if (kotlin.math.abs(closest - target) > kotlin.math.abs(current.`val` - target)) {
                closest = current.`val`
            }
            if (current.`val`.toDouble() == target) {
                return current.`val`
            }
            current = if (target < current.`val`) current.left else current.right
        }
        return closest
    }
}
