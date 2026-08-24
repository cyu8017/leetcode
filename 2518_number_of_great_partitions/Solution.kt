// LeetCode 2518 - Number of Great Partitions
// https://leetcode.com/problems/number-of-great-partitions/

class Solution {
    fun countPartitions(nums: IntArray, k: Int): Int {
            var MOD: Int = 1000000007
            var sum: Long = 0
            for (x in nums) sum += x
            if (sum < 2L * k) return 0
            var dp: IntArray = IntArray(k)
            dp[0] = 1
            for (x in nums) {
                var s: Int = k - 1
    while (s >= x) {
    
                    dp[s] = (dp[s] + dp[s - x]) % MOD
    s = s - 1
    }
            }
            var bad: Int = 0
            for (v in dp) bad = (bad + v) % MOD
            var total: Int = 1
            var i: Int = 0
    while (i < nums.size) {
    total = total * 2 % MOD
    i = i + 1
    }
            return ((total - 2L * bad % MOD + MOD) % MOD)
    }
}
