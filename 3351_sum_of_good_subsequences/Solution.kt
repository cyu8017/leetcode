// LeetCode 3351 - Sum of Good Subsequences
// https://leetcode.com/problems/sum-of-good-subsequences/

class Solution {
    fun sumOfGoodSubsequences(nums: IntArray): Int {
        val mod = 1_000_000_007
        var cnt = HashMap<Int, Int>()
        var sum = HashMap<Int, Int>()
        var ans = 0
        for (x in nums) {
            var c = 1
            var s = x
            if (cnt.getOrDefault(x - 1, 0) > 0) {
                c = (c + cnt[x - 1]) % mod
                s = ((s + sum[x - 1] + cnt[x - 1] * x % mod) % mod)
            }
            if (cnt.getOrDefault(x + 1, 0) > 0) {
                c = (c + cnt[x + 1]) % mod
                s = ((s + sum[x + 1] + cnt[x + 1] * x % mod) % mod)
            }
            cnt[x] = (cnt.getOrDefault(x, 0 + c) % mod)
            sum[x] = (sum.getOrDefault(x, 0 + s) % mod)
            ans = (ans + s) % mod
        }
        return ans
    }
}
