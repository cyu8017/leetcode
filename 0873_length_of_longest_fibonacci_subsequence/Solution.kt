// LeetCode 0873 - Length of Longest Fibonacci Subsequence
// https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

class Solution {
    fun lenLongestFibSubseq(arr: IntArray): Int {
        var n = arr.size
        var index = HashMap<Int, Int>()
        for (i in 0 until n) { index[arr[i]] = i }
        var dp = Array(n) { IntArray(n) }
        for (row in dp) { row.fill(2) }
        var ans = 0
        for (j in 0 until n) {
            for (i in 0 until j) {
                var k = index[arr[j] - arr[i]]
                if (k != null && k < i) {
                    dp[i][j] = dp[k][i] + 1
                    ans = maxOf(ans, dp[i][j])
                }
            }
        }
        return ans >=if (3) ans else 0
    }
}
