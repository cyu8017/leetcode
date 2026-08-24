// LeetCode 2912 - Number of Ways to Reach Destination in the Grid
// https://leetcode.com/problems/number-of-ways-to-reach-destination-in-the-grid/

class Solution {
    fun numberOfWays(n: Int, m: Int, k: Int, source: IntArray, dest: IntArray): Int {
        val mod = 1000000007
        var sx = source[0]
        var sy = source[1]
        var tx = dest[0]
        var ty = dest[1]
        var same = 0
        var row = 0
        var col = 0
        var other = 0
        if (sx == tx && sy == ty) same = 1
        else if (sx == tx) row = 1
        else if (sy == ty) col = 1
        else other = 1
        for (step in 0 until k) {
            var ns = (row * (m - 1) + col * (n - 1)) % mod
            var nr = (same + row * (m - 2) % mod + other * (n - 1) % mod) % mod
            var nc = (same + col * (n - 2) % mod + other * (m - 1) % mod) % mod
            var no = (row * (n - 1) + col * (m - 1) + other * (n + m - 4) % mod) % mod
            same = ns
            row = nr
            col = nc
            other = no
        }
        if (sx == tx && sy == ty) return (int) same
        if (sx == tx) return (int) row
        if (sy == ty) return (int) col
        return other
    }
}
