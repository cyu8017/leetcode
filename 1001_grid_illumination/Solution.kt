// LeetCode 1001 - Grid Illumination
// https://leetcode.com/problems/grid-illumination/

class Solution {
    fun gridIllumination(n: Int, lamps: Array<IntArray>, queries: Array<IntArray>): IntArray {
        val rows = mutableMapOf<Int, Int>()
        val cols = mutableMapOf<Int, Int>()
        val diag1 = mutableMapOf<Int, Int>()
        val diag2 = mutableMapOf<Int, Int>()
        val lit = mutableSetOf<Long>()
        fun key(r: Int, c: Int) = (r.toLong() shl 32) or (c.toLong() and 0xffffffffL)
        fun dec(map: MutableMap<Int, Int>, k: Int) {
            val v = (map[k] ?: 0) - 1
            if (v <= 0) map.remove(k) else map[k] = v
        }
        for (lamp in lamps) {
            val r = lamp[0]; val c = lamp[1]
            if (!lit.add(key(r, c))) continue
            rows[r] = (rows[r] ?: 0) + 1
            cols[c] = (cols[c] ?: 0) + 1
            diag1[r - c] = (diag1[r - c] ?: 0) + 1
            diag2[r + c] = (diag2[r + c] ?: 0) + 1
        }
        val ans = IntArray(queries.size)
        for (qi in queries.indices) {
            val r = queries[qi][0]; val c = queries[qi][1]
            if ((rows[r] ?: 0) > 0 || (cols[c] ?: 0) > 0 || (diag1[r - c] ?: 0) > 0 || (diag2[r + c] ?: 0) > 0) {
                ans[qi] = 1
            }
            for (i in r - 1..r + 1) {
                for (j in c - 1..c + 1) {
                    if (lit.remove(key(i, j))) {
                        dec(rows, i); dec(cols, j); dec(diag1, i - j); dec(diag2, i + j)
                    }
                }
            }
        }
        return ans
    }
}
