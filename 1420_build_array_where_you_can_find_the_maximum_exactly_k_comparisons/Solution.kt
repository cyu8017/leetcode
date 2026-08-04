// LeetCode 1420 - Build Array Where You Can Find The Maximum Exactly K Comparisons
// https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/

class Solution {
    fun numOfArrays(n: Int, m: Int, k: Int): Int {
        val mod = 1_000_000_007
        var dp = Array(k + 1) { IntArray(m + 1) }
        for (maximum in 1..m) dp[1][maximum] = 1
        for (len in 1 until n) {
            val nxt = Array(k + 1) { IntArray(m + 1) }
            for (cost in 1..k) {
                var prefix = 0
                for (maximum in 1..m) {
                    prefix = (prefix + dp[cost - 1][maximum - 1]) % mod
                    nxt[cost][maximum] = ((maximum.toLong() * dp[cost][maximum] + prefix) % mod).toInt()
                }
            }
            dp = nxt
        }
        var answer = 0
        for (v in dp[k]) answer = (answer + v) % mod
        return answer
    }
}
