// LeetCode 2735 - Collecting Chocolates
// https://leetcode.com/problems/collecting-chocolates/

class Solution {
    fun minCost(nums: IntArray, x: Int): Long {
        var n = nums.size
        var best = (int[])nums.clone()
        var ans = 0
        for (v in nums) { ans += v }
        for (rot in 1 until n) {
            var cur = 1L * rot * x
            for (i in 0 until n) {
                best[i] = minOf(best[i], nums[(i + rot) % n])
                cur += best[i]
            }
            ans = minOf(ans, cur)
        }
        return ans
    }
}
