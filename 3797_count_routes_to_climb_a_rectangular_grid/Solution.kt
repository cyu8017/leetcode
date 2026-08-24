// LeetCode 3797 - Count Routes To Climb A Rectangular Grid
// https://leetcode.com/problems/count_routes_to_climb_a_rectangular_grid/

class Solution {
    fun countRoutes(grid: Array<String>, d: Int): Int {
        val MOD = 1_000_000_007
        var n = grid.size
        var m = grid[0].size
        var upRadius = 0
        while ((upRadius + 1) * (upRadius + 1) + 1 <= d * d) { upRadius += 1 }
        var arrived = IntArray(m)
        for (c in 0 until m) {
            if (grid[n - 1][c] == '.') arrived[c] = 1
        }
        for (r in n - 1 downTo 0) {
            var pref = IntArray(m + 1)
            for (i in 0 until m) { pref[i + 1] = (pref[i] + arrived[i]) % MOD }
            var horizontal = IntArray(m)
            for (c in 0 until m) {
                if (grid[r][c] == '#') continue
                var l = maxOf(0, c - d)
                var rr = minOf(m - 1, c + d)
                horizontal[c] = (pref[rr + 1] - pref[l] - arrived[c]) % MOD
                if (horizontal[c] < 0) horizontal[c] += MOD
            }
            if (r == 0) {
                var ans = 0
                for (c in 0 until m) { ans = (ans + arrived[c] + horizontal[c]) % MOD }
                return ans
            }
            var pref2 = IntArray(m + 1)
            for (c in 0 until m) { pref2[c + 1] = (pref2[c] + arrived[c] + horizontal[c]) % MOD }
            var next = IntArray(m)
            for (c in 0 until m) {
                if (grid[r - 1][c] == '#') continue
                var l = maxOf(0, c - upRadius)
                var rr = minOf(m - 1, c + upRadius)
                next[c] = pref2[rr + 1] - pref2[l]
                if (next[c] < 0) next[c] += MOD
            }
            arrived = next
        }
        return 0
    }
}
