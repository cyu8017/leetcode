// LeetCode 1923
// https://leetcode.com/problems/longest-common-subpath/

class Solution {
    fun longestCommonSubpath(n: Int, paths: Array<IntArray>): Int {
        val base1 = 911382323L
        val mod1 = 1_000_000_007L
        val base2 = 972663749L
        val mod2 = 1_000_000_009L

        fun modPow(base: Long, exp: Int, mod: Long): Long {
            var b = base % mod
            var e = exp
            var res = 1L
            while (e > 0) {
                if (e and 1 == 1) res = res * b % mod
                b = b * b % mod
                e = e shr 1
            }
            return res
        }

        fun hasCommon(length: Int): Boolean {
            if (length == 0) return true
            var common: HashSet<Long>? = null
            val pow1 = modPow(base1, length, mod1)
            val pow2 = modPow(base2, length, mod2)
            for (path in paths) {
                if (path.size < length) return false
                var h1 = 0L
                var h2 = 0L
                val seen = HashSet<Long>()
                for (i in path.indices) {
                    h1 = (h1 * base1 + path[i] + 1) % mod1
                    h2 = (h2 * base2 + path[i] + 1) % mod2
                    if (i >= length) {
                        h1 = (h1 - (path[i - length] + 1) * pow1 % mod1 + mod1) % mod1
                        h2 = (h2 - (path[i - length] + 1) * pow2 % mod2 + mod2) % mod2
                    }
                    if (i >= length - 1) seen.add((h1 shl 32) xor h2)
                }
                common = if (common == null) seen else common!!.also { it.retainAll(seen) }
                if (common!!.isEmpty()) return false
            }
            return true
        }

        var lo = 0
        var hi = paths.minOf { it.size }
        while (lo < hi) {
            val mid = (lo + hi + 1) / 2
            if (hasCommon(mid)) lo = mid else hi = mid - 1
        }
        return lo
    }
}
