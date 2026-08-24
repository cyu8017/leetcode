// LeetCode 2466 - Count Ways To Build Good Strings
// https://leetcode.com/problems/count-ways-to-build-good-strings/

class Solution {
    fun countGoodStrings(low: Int, high: Int, zero: Int, one: Int): Int {
            var mod: Int = 1000000007
            var dp: IntArray = IntArray(high + 1)
            dp[0] = 1
            var ans: Int = 0
            var i: Int = 1
    while (i <= high) {
    
                if (i >= zero) dp[i] = (dp[i] + dp[i - zero]) % mod
                if (i >= one) dp[i] = (dp[i] + dp[i - one]) % mod
                if (i >= low) ans = (ans + dp[i]) % mod
    
    i = i + 1
    }
            return ans
    }
}
