// LeetCode 3686 - Number of Stable Subsequences
// https://leetcode.com/problems/number-of-stable-subsequences/

class Solution {
    fun countStableSubsequences(nums: IntArray): Int {
        var MOD = 1000000007
        var a1 = 0
        var a2 = 0
        var b1 = 0
        var b2 = 0
        for (x in nums) {
            if (x % 2 == 1) {
                var na1 = (1 + b1 + b2) % MOD
                var na2 = a1
                a1 = (a1 + na1) % MOD
                a2 = (a2 + na2) % MOD
            } else {
                var nb1 = (1 + a1 + a2) % MOD
                var nb2 = b1
                b1 = (b1 + nb1) % MOD
                b2 = (b2 + nb2) % MOD
            }
        }
        return (((a1 + a2) % MOD + b1) % MOD + b2) % MOD
    }
}
