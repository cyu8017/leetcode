// LeetCode 3987 - Minimum Total Cost to Process All Elements
// https://leetcode.com/problems/minimum-total-cost-to-process-all-elements/

class Solution {
    fun minimumCost(nums: IntArray, k: Int): Int {
        val mod = 1000000007L
        var cnt = 0
        var cur = k
        for (x0 in nums) {
            var x = x0
            var diff = x - cur
            if (diff > 0) {
                var m = (diff + k - 1) / k
                cur += m * k
                cnt += m
            }
            cur -= x
        }
        cnt %= mod
        return ((cnt + 1) * cnt / 2 % mod)
    }
}
