// LeetCode 3287 - Find the Maximum Sequence Value of Array
// https://leetcode.com/problems/find-the-maximum-sequence-value-of-array/

class Solution {
    fun maxValue(nums: IntArray, k: Int): Int {
        val n = nums.size
        val MAX = 128
        val left = Array(n + 1) { Array(k + 1) { BooleanArray(MAX) } }
        left[0][0][0] = true
        for (i in 0 until n) {
            for (j in 0..k) {
                for (v in 0 until MAX) {
                    if (!left[i][j][v]) continue
                    left[i + 1][j][v] = true
                    if (j < k) left[i + 1][j + 1][v or nums[i]] = true
                }
            }
        }
        val right = Array(n + 1) { Array(k + 1) { BooleanArray(MAX) } }
        right[n][0][0] = true
        for (i in n - 1 downTo 0) {
            for (j in 0..k) {
                for (v in 0 until MAX) {
                    if (!right[i + 1][j][v]) continue
                    right[i][j][v] = true
                    if (j < k) right[i][j + 1][v or nums[i]] = true
                }
            }
        }
        var ans = 0
        var mid = k
        while (mid + k <= n) {
            for (a in 0 until MAX) {
                if (!left[mid][k][a]) continue
                for (b in 0 until MAX) {
                    if (right[mid][k][b] && (a xor b) > ans) ans = a xor b
                }
            }
            mid++
        }
        return ans
    }
}
