// LeetCode 2902 - Count of Sub-Multisets With Bounded Sum
// https://leetcode.com/problems/count-of-sub-multisets-with-bounded-sum/


class Solution {
    fun countSubMultisets(nums: IntArray, l: Int, r0: Int): Int {
        val mod = 1_000_000_007
        val freq = HashMap<Int, Int>()
        var total = 0
        for (v in nums) {
            freq[v] = freq.getOrDefault(v, 0) + 1
            total += v
        }
        if (total < l) return 0
        var r = r0
        if (r > total) r = total
        var dp = IntArray(r + 1)
        dp[0] = 1
        val zeros = freq.getOrDefault(0, 0)
        freq.remove(0)
        for ((v, c) in freq) {
            val ndp = IntArray(r + 1)
            for (sum in 0..r) {
                if (dp[sum] == 0) continue
                var k = 0
                while (k <= c && sum + k * v <= r) {
                    ndp[sum + k * v] = (ndp[sum + k * v] + dp[sum]) % mod
                    k++
                }
            }
            dp = ndp
        }
        var ans = 0
        for (s in l..r) ans = (ans + dp[s]) % mod
        ans = (1L * ans * (zeros + 1) % mod).toInt()
        return ans
    }
}
