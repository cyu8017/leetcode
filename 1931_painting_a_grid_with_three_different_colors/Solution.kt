// LeetCode 1931
// https://leetcode.com/problems/painting-a-grid-with-three-different-colors/

class Solution {
    fun colorTheGrid(m: Int, n: Int): Int {
        val mod = 1_000_000_007
        fun validColumn(mask0: Int): Boolean {
            var mask = mask0
            var prev = -1
            repeat(m) {
                val c = mask % 3
                if (c == prev) return false
                prev = c
                mask /= 3
            }
            return true
        }
        fun getColors(mask0: Int): IntArray {
            var mask = mask0
            val cols = IntArray(m)
            for (i in 0 until m) {
                cols[i] = mask % 3
                mask /= 3
            }
            return cols
        }
        val maxState = Math.pow(3.0, m.toDouble()).toInt()
        val states = (0 until maxState).filter { validColumn(it) }
        val compat = HashMap<Int, MutableList<Int>>()
        for (a in states) {
            val ca = getColors(a)
            compat[a] = mutableListOf()
            for (b in states) {
                val cb = getColors(b)
                if ((0 until m).all { ca[it] != cb[it] }) compat[a]!!.add(b)
            }
        }
        val memo = HashMap<Long, Int>()
        fun dp(col: Int, prev: Int): Int {
            if (col == n) return 1
            val key = col.toLong() shl 32 or (prev.toLong() and 0xffffffffL)
            memo[key]?.let { return it }
            var total = 0
            val options = if (prev == -1) states else compat[prev]!!
            for (cur in options) total = (total + dp(col + 1, cur)) % mod
            memo[key] = total
            return total
        }
        return dp(0, -1)
    }
}
