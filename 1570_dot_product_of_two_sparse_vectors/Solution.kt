// LeetCode 1570 - Dot Product of Two Sparse Vectors
// https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

class SparseVector(nums: IntArray) {
    private val values = HashMap<Int, Int>()

    init {
        for (i in nums.indices) {
            if (nums[i] != 0) values[i] = nums[i]
        }
    }

    fun dotProduct(vec: SparseVector): Int {
        if (values.size > vec.values.size) return vec.dotProduct(this)
        var sum = 0
        for ((key, value) in values) {
            sum += value * vec.values.getOrDefault(key, 0)
        }
        return sum
    }
}

class Solution {
    fun dotProduct(nums1: IntArray, nums2: IntArray): Int =
        SparseVector(nums1).dotProduct(SparseVector(nums2))
}
