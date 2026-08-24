// LeetCode 2679 - Sum in a Matrix
// https://leetcode.com/problems/sum-in-a-matrix/

class Solution {
    fun matrixSum(nums: Array<IntArray>): Int {
        for (row in nums) row.sort()
        var ans = 0
        val n = nums[0].size
        for (j in 0 until n) {
            var mx = 0
            for (row in nums) mx = maxOf(mx, row[j])
            ans += mx
        }
        return ans
    }
}
