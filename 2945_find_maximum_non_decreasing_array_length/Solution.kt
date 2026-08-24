// LeetCode 2945 - Find Maximum Non-decreasing Array Length
// https://leetcode.com/problems/find-maximum-non-decreasing-array-length/

class Solution {
    fun findMaximumLength(nums: IntArray): Int {
        var n = nums.size
        var pref = LongArray(n + 1)
        var last = LongArray(n + 1)
        for (i in 0 until n) { pref[i + 1] = pref[i] + nums[i] }
        var dp = IntArray(n + 1)
        var dq = ArrayList<LongArray>()
        dq.add(longArrayOf(0, 0))
        for (i in 1..n) {
            while (dq.size > 1 && dq[1][1] <= pref[i]) dq.remove(0)
            var j = dq[0][0]
            dp[i] = dp[j] + 1
            last[i] = pref[i] - pref[j]
            var `val` = pref[i] + last[i]
            while (!dq.isEmpty() && dq[dq.size - 1][1] >= val) dq.removeAt(dq.size - 1)
            dq.add(longArrayOf(i, val))
        }
        return dp[n]
    }
}
