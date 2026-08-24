// LeetCode 0108 - Convert Sorted Array to Binary Search Tree
// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun sortedArrayToBST(nums: IntArray): TreeNode? {
        return build(nums, 0, nums.size - 1)
    }

    private fun build(nums: IntArray, left: Int, right: Int): TreeNode? {
        if (left > right) {
            return null
        }
        val mid = (left + right + 1) / 2
        val root = TreeNode(nums[mid])
        root.left = build(nums, left, mid - 1)
        root.right = build(nums, mid + 1, right)
        return root
    }
}
