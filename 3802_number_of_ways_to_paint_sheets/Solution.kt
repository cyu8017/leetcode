// LeetCode 3802 - Number Of Ways To Paint Sheets
// https://leetcode.com/problems/number_of_ways_to_paint_sheets/

class Solution {
    fun numberOfWays(n: Int, limit: IntArray): Int {
        val MOD = 1_000_000_007L
        limit.sort()
        val points = ArrayList<Int>()
        points.add(1)
        points.add(n)
        for (x in limit) {
            if (x + 1 > 1 && x + 1 < n) points.add(x + 1)
            if (n - x > 1 && n - x < n) points.add(n - x)
        }
        points.sort()
        var u = 0
        for (i in points.indices) {
            if (u == 0 || points[i] != points[u - 1]) {
                points[u++] = points[i]
            }
        }
        val uniq = points.subList(0, u)
        var ans = 0L
        for (i in 0 until uniq.size - 1) {
            val x = uniq[i]
            val a = countGE(limit, x)
            val b = countGE(limit, n - x)
            val same = countGE(limit, maxOf(x, n - x))
            val ways = (a * b - same) % MOD
            val length = (uniq[i + 1] - x).toLong()
            ans = (ans + ways * length) % MOD
        }
        if (ans < 0) ans += MOD
        return ans.toInt()
    }

    private fun countGE(limit: IntArray, x: Int): Long {
        var lo = 0
        var hi = limit.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (limit[mid] < x) lo = mid + 1 else hi = mid
        }
        return (limit.size - lo).toLong()
    }
}
