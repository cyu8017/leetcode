// LeetCode 3858 - Minimum Bitwise Or From Grid
// https://leetcode.com/problems/minimum-bitwise-or-from-grid/

class Solution {
    private fun bitLen(x0: Int): Int {
        var x = x0
        if (x == 0) return 0
        var n = 0
        while (x > 0) {
            n++
            x = x shr 1
        }
        return n
    }

    fun minimumOR(grid: Array<IntArray>): Int {
        var mx = 0
        for (row in grid) for (x in row) mx = maxOf(mx, x)
        val m = bitLen(mx)
        var ans = 0
        for (i in m - 1 downTo 0) {
            val mask = ans or ((1 shl i) - 1)
            for (row in grid) {
                var found = false
                for (x in row) {
                    if ((x or mask) == mask) {
                        found = true
                        break
                    }
                }
                if (!found) {
                    ans = ans or (1 shl i)
                    break
                }
            }
        }
        return ans
    }
}
