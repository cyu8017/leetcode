// LeetCode 3250 - Find the Count of Monotonic Pairs I
// https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/

class Solution {
    fun countOfPairs(nums: IntArray): Int {
        val mod = 1000000007
        var n = nums.size
        var dp = IntArray(51)
        for (a in 0 ..nums[0]) { dp[a] = 1 }
        for (i in 1 until n) {
            var ndp = IntArray(51)
            var pref = IntArray(52)
            for (a in 0 ..50) { pref[a + 1] = (pref[a] + dp[a]) % mod }
            for (a2 in 0 ..nums[i]) {
                var b2 = nums[i] - a2
                var maxA1 = a2
                var lim = nums[i - 1] - b2
                if (lim < maxA1) maxA1 = lim
                if (maxA1 < 0) continue
                if (maxA1 > 50) maxA1 = 50
                ndp[a2] = pref[maxA1 + 1]
            }
            dp = ndp
        }
        var ans = 0
        for (v in dp) { ans = (ans + v) % mod }
        return ans
    }
}
