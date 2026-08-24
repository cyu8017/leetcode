// LeetCode 3193 - Count the Number of Inversions
// https://leetcode.com/problems/count-the-number-of-inversions/

class Solution {
    fun numberOfPermutations(n: Int, requirements: Array<IntArray>): Int {
        var req = IntArray(n)
        req.fill(-1)
        for (var r : requirements) req[r[0]] = r[1]
        if (req[0] > 0) return 0
        req[0] = 0
        var m = 0
        for (v in req) { m = maxOf(m, v) }
        val mod = 1000000007
        var f = IntArray(n)[]
        for (i in 0 until n) { f[i] = IntArray(m + 1) }
        f[0][0] = 1
        for (i in 1 until n) {
            var l = 0
            var r = m
            if (req[i] >= 0) l = r = req[i]
            for (j in l ..r) {
                for (k in 0 ..minOf(i, j)) {
                    f[i][j] = (f[i][j] + f[i - 1][j - k]) % mod
                }
            }
        }
        return f[n - 1][req[n - 1]]
    }
}
