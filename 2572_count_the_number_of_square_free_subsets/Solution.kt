// LeetCode 2572 - Count the Number of Square-Free Subsets
// https://leetcode.com/problems/count-the-number-of-square-free-subsets/

class Solution {
    private val MOD = 1_000_000_007
    private val PRIMES = intArrayOf(2, 3, 5, 7, 11, 13, 17, 19, 23, 29)

    fun squareFreeSubsets(nums: IntArray): Int {
        val freq = HashMap<Int, Int>()
        for (x in nums) freq[x] = freq.getOrDefault(x, 0) + 1
        val dp = IntArray(1 shl 10)
        dp[0] = 1
        for ((x, c) in freq) {
            if (x == 1) continue
            val m = maskOf(x)
            if (m < 0) continue
            for (state in (1 shl 10) - 1 downTo 0) {
                if ((state and m) == 0) {
                    dp[state or m] = ((dp[state or m] + dp[state].toLong() * c) % MOD).toInt()
                }
            }
        }
        var ans = 0
        for (v in dp) ans = (ans + v) % MOD
        val ones = freq.getOrDefault(1, 0)
        var mul = 1
        repeat(ones) { mul = mul * 2 % MOD }
        ans = ((ans.toLong() * mul) % MOD).toInt()
        ans = (ans - 1 + MOD) % MOD
        return ans
    }

    private fun maskOf(x0: Int): Int {
        var x = x0
        var mask = 0
        for (i in PRIMES.indices) {
            val p = PRIMES[i]
            var cnt = 0
            while (x % p == 0) {
                x /= p
                cnt += 1
                if (cnt > 1) return -1
            }
            if (cnt == 1) mask = mask or (1 shl i)
        }
        return mask
    }
}
