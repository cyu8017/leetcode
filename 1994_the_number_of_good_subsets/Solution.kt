// LeetCode 1994
// https://leetcode.com/problems/the-number-of-good-subsets/

class Solution {
    fun numberOfGoodSubsets(nums: IntArray): Int {
        val mod = 1_000_000_007L
        val primes = intArrayOf(2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
        val masks = IntArray(31)
        for (x in 2..30) {
            var m = 0
            var y = x
            var ok = true
            for (i in primes.indices) {
                val p = primes[i]
                if (y % p == 0) {
                    if ((y / p) % p == 0) {
                        ok = false
                        break
                    }
                    m = m or (1 shl i)
                    y /= p
                }
            }
            masks[x] = if (ok) m else -1
        }
        val cnt = IntArray(31)
        for (v in nums) cnt[v]++
        val dp = LongArray(1 shl primes.size)
        dp[0] = 1
        for (x in 2..30) {
            if (cnt[x] == 0 || masks[x] < 0) continue
            val m = masks[x]
            for (state in (1 shl primes.size) - 1 downTo 0) {
                if (state and m != 0) continue
                dp[state or m] = (dp[state or m] + dp[state] * cnt[x]) % mod
            }
        }
        var ans = 0L
        for (i in 1 until dp.size) ans = (ans + dp[i]) % mod
        fun modPow(base: Long, exp: Int): Long {
            var b = base
            var e = exp
            var res = 1L
            while (e > 0) {
                if (e and 1 == 1) res = res * b % mod
                b = b * b % mod
                e = e shr 1
            }
            return res
        }
        ans = ans * modPow(2, cnt[1]) % mod
        return ans.toInt()
    }
}
