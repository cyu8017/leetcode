// LeetCode 3299 - Sum of Consecutive Subsequences
// https://leetcode.com/problems/sum-of-consecutive-subsequences/

class Solution {
    fun rangeSum(nums: IntArray): Int {
        val mod = 1_000_000_007
        var cnt = HashMap<Int, Int>()
        var sum = HashMap<Int, Int>()
        var ans = 0
        for (x in nums) {
            var cL = cnt.getOrDefault(x - 1, 0), sL = sum.getOrDefault(x - 1, 0)
            var cR = cnt.getOrDefault(x + 1, 0), sR = sum.getOrDefault(x + 1, 0)
            var c = (1 + cL + cR) % mod
            var s = ((x + sL + cL * x % mod + sR + cR * x % mod) % mod)
            if (cL > 0 && cR > 0) {
                c = (c + (cL * cR % mod)) % mod
                s = ((s + sL * cR % mod + sR * cL % mod + cL * cR % mod * x % mod) % mod)
            }
            cnt[x] = (cnt.getOrDefault(x, 0 + c) % mod)
            sum[x] = (sum.getOrDefault(x, 0 + s) % mod)
            ans = (ans + s) % mod
        }
        return ans
    }
}
