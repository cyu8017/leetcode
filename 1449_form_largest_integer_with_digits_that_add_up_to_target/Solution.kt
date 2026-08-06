// LeetCode 1449 - Form Largest Integer With Digits That Add up to Target
// https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/

class Solution {
    fun largestNumber(cost: IntArray, target: Int): String {
        val dp = arrayOfNulls<String>(target + 1)
        dp[0] = ""
        for (total in 1..target) {
            var best: String? = null
            for (digit in 1..9) {
                val price = cost[digit - 1]
                if (total >= price && dp[total - price] != null) {
                    val candidate = digit.toString() + dp[total - price]
                    if (best == null || candidate.length > best.length ||
                        (candidate.length == best.length && candidate > best)
                    ) {
                        best = candidate
                    }
                }
            }
            dp[total] = best
        }
        return dp[target] ?: "0"
    }
}
