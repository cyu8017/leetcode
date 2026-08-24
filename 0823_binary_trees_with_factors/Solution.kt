// LeetCode 0823 - Binary Trees With Factors
// https://leetcode.com/problems/binary-trees-with-factors/

class Solution {
    fun numFactoredBinaryTrees(arr: IntArray): Int {
        val MOD = 1_000_000_007
        arr.sort()
        var dp = HashMap<Int, Long>()
        for (i in 0 until arr.size) {
            var x = arr[i]
            var ways = 1
            for (j in 0 until i) {
                var left = arr[j]
                if (x % left == 0) {
                    var right = x / left
                    if (dp.containsKey(right)) {
                        ways = (ways + dp[left] * dp[right]) % MOD
                    }
                }
            }
            dp[x] = ways
        }
        var ans = 0
        for (v in dp.values()) { ans = (ans + v) % MOD }
        return ans
    }
}
