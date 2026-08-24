// LeetCode 3348 - Smallest Divisible Digit Product II
// https://leetcode.com/problems/smallest-divisible-digit-product-ii/

class Solution {
    private fun dfs(res: CharArray, i: Int, tight: Boolean, sameLen: Boolean, num: String, t: Long): Boolean {
        if (i == res.size) {
            var prod = 1L
            for (c in res) {
                prod *= (c - '0').toLong()
                if (prod == 0L) break
            }
            return prod % t == 0L && prod > 0L
        }
        var start = if (i == 0) '1' else '0'
        if (tight && sameLen && i < num.length) start = num[i]
        var c = start
        while (c <= '9') {
            res[i] = c
            val nt = tight && sameLen && i < num.length && c == num[i]
            if (dfs(res, i + 1, nt, sameLen, num, t)) return true
            c++
        }
        return false
    }

    fun smallestNumber(num: String, t: Long): String {
        var tt = t
        for (d in 9 downTo 2) {
            while (tt % d == 0L) tt /= d
        }
        if (tt > 1L) return "-1"
        for (extra in 0..60) {
            val L = num.length + extra
            val res = CharArray(L)
            if (dfs(res, 0, true, extra == 0, num, t)) return String(res)
        }
        return "-1"
    }
}
