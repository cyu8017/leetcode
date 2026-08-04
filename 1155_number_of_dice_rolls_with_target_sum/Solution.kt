// LeetCode 1155 - Number of Dice Rolls With Target Sum
// https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

class Solution {
    fun numRollsToTarget(n: Int, k: Int, target: Int): Int {
        val MOD = 1_000_000_007
        var dp = IntArray(target + 1)
        dp[0] = 1
        repeat(n) {
            val new = IntArray(target + 1)
            for (s in 0..target) {
                if (dp[s] == 0) continue
                for (face in 1..k) {
                    if (s + face <= target) {
                        new[s + face] = (new[s + face] + dp[s]) % MOD
                    }
                }
            }
            dp = new
        }
        return dp[target]
    }
}
