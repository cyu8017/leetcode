// LeetCode 1397 - Find All Good Strings
// https://leetcode.com/problems/find-all-good-strings/

class Solution {
    fun findGoodStrings(n: Int, s1: String, s2: String, evil: String): Int {
        val mod = 1_000_000_007
        val m = evil.length
        val pi = IntArray(m)
        for (i in 1 until m) {
            var j = pi[i - 1]
            while (j > 0 && evil[i] != evil[j]) j = pi[j - 1]
            if (evil[i] == evil[j]) j++
            pi[i] = j
        }
        val trans = Array(m) { IntArray(26) }
        for (j in 0 until m) {
            for (x in 0 until 26) {
                val c = ('a'.code + x).toChar()
                var k = j
                while (k > 0 && evil[k] != c) k = pi[k - 1]
                if (evil[k] == c) k++
                trans[j][x] = k
            }
        }
        val memo = HashMap<Long, Int>()
        fun key(i: Int, j: Int, lo: Boolean, hi: Boolean): Long {
            return (((i.toLong() * (m + 1) + j) * 2 + if (lo) 1 else 0) * 2) + if (hi) 1 else 0
        }
        fun dp(i: Int, j: Int, lo: Boolean, hi: Boolean): Int {
            if (j == m) return 0
            if (i == n) return 1
            val memoKey = key(i, j, lo, hi)
            memo[memoKey]?.let { return it }
            val a = if (lo) s1[i] - 'a' else 0
            val b = if (hi) s2[i] - 'a' else 25
            var ans = 0
            for (x in a..b) {
                ans = (ans + dp(i + 1, trans[j][x], lo && x == a, hi && x == b)) % mod
            }
            memo[memoKey] = ans
            return ans
        }
        return dp(0, 0, true, true)
    }
}
