// LeetCode 2905 - Find Indices With Index and Value Difference II
// https://leetcode.com/problems/find-indices-with-index-and-value-difference-ii/

class Solution {
    fun findIndices(nums: IntArray, indexDifference: Int, valueDifference: Int): IntArray {
        var n = nums.size
        var minIdx = 0
        var maxIdx = 0
        for (j in indexDifference until n) {
            var i = j - indexDifference
            if (nums[i] < nums[minIdx]) minIdx = i
            if (nums[i] > nums[maxIdx]) maxIdx = i
            if (nums[j] - nums[minIdx] >= valueDifference) return intArrayOf(minIdx, j)
            if (nums[maxIdx] - nums[j] >= valueDifference) return intArrayOf(maxIdx, j)
        }
        return intArrayOf(-1, -1)
    }
}
