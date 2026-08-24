// LeetCode 2152 - Minimum Number of Lines to Cover Points
// https://leetcode.com/problems/minimum-number-of-lines-to-cover-points/

class Solution {
    fun colinear(a: IntArray, b: IntArray, c: IntArray): Boolean {
        return (b[0] - a[0]) * (c[1] - a[1]) == (c[0] - a[0]) * (b[1] - a[1])
    }

    fun minimumLines(points: Array<IntArray>): Int {
        var n: Int = points.size
        if (n <= 2) return 1
        var inf: Int = n
        var dp: IntArray = IntArray(1 << n)
        dp.fill(inf)
        dp[0] = 0
        for (mask in 0 until (1 << n)) {
            if (dp[mask] == inf) continue
            var i: Int = 0
            while (i < n && (mask & (1 << i)) != 0) i++
            if (i == n) continue
            var nm: Int = mask | (1 << i)
            dp[nm] = minOf(dp[nm], dp[mask] + 1)
            for (j in i + 1 until n) {
                if ((mask & (1 << j)) != 0) continue
                nm = mask | (1 << i) | (1 << j)
                for (k in 0 until n)
                    if ((nm & (1 << k)) == 0 && colinear(points[i], points[j], points[k]))
                        nm |= 1 << k
                dp[nm] = minOf(dp[nm], dp[mask] + 1)
            }
        }
        return dp[(1 << n) - 1]
    }
}
