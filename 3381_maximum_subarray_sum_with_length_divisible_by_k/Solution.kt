// LeetCode 3381 - Maximum Subarray Sum With Length Divisible by K
// https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

class Solution {
    fun maxSubarraySum(nums: IntArray, k: Int): Long {
        var n = nums.size
        var pref = LongArray(n + 1)
        for (i in 0 until n) { pref[i + 1] = pref[i] + nums[i] }
        val INF = 1L  shl  62
        var best = LongArray(k)
        for (i in 0 until k) { best[i] = INF }
        best[0] = 0
        var ans = -(1L  shl  62)
        for (i in 1 ..n) {
            var r = i % k
            if (best[r] != INF) {
                var cand = pref[i] - best[r]
                if (cand > ans) ans = cand
            }
            if (pref[i] < best[r]) best[r] = pref[i]
        }
        return ans
    }
}
