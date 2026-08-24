// LeetCode 0654 - Maximum Binary Tree
// https://leetcode.com/problems/maximum-binary-tree/

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun constructMaximumBinaryTree(nums: IntArray): TreeNode? {
        fun build(left: Int, right: Int): TreeNode? {
            if (left > right) return null
            var maxIdx = left
            for (i in left..right) if (nums[i] > nums[maxIdx]) maxIdx = i
            val node = TreeNode(nums[maxIdx])
            node.left = build(left, maxIdx - 1)
            node.right = build(maxIdx + 1, right)
            return node
        }
        return build(0, nums.size - 1)
    }
}
