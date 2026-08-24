// LeetCode 3355 - Zero Array Transformation I
// https://leetcode.com/problems/zero-array-transformation-i/

class Solution {
    fun isZeroArray(nums: IntArray, queries: Array<IntArray>): Boolean {
        var n = nums.size
        var diff = IntArray(n + 1)
        for (q in queries) {
            diff[q[0]]++
            diff[q[1] + 1]--
        }
        var cur = 0
        for (i in 0 until n) {
            cur += diff[i]
            if (cur < nums[i]) return false
        }
        return true
    }
}
