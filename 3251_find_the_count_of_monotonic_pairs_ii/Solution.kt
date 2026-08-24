// LeetCode 3251 - Find the Count of Monotonic Pairs II
// https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/

class Solution {
    fun countOfPairs(nums: IntArray): Int {
        val mod = 1000000007
        var n = nums.size
        var maxV = 0
        for (v in nums) { maxV = maxOf(maxV, v) }
        var dp = IntArray(maxV + 1)
        for (a in 0 ..nums[0]) { dp[a] = 1 }
        for (i in 1 until n) {
            var ndp = IntArray(maxV + 1)
            var pref = IntArray(maxV + 2)
            for (a in 0 ..maxV) { pref[a + 1] = (pref[a] + dp[a]) % mod }
            for (a2 in 0 ..nums[i]) {
                var b2 = nums[i] - a2
                var maxA1 = a2
                var lim = nums[i - 1] - b2
                if (lim < maxA1) maxA1 = lim
                if (maxA1 < 0) continue
                if (maxA1 > maxV) maxA1 = maxV
                ndp[a2] = pref[maxA1 + 1]
            }
            dp = ndp
        }
        var ans = 0
        for (v in dp) { ans = (ans + v) % mod }
        return ans
    }
}
