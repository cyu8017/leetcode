// LeetCode 3257 - Maximum Value Sum by Placing Three Rooks II
// https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-ii/

class Solution {
    private class Cell(val v: Int, val c: Int)

    fun maximumValueSum(board: Array<IntArray>): Long {
        val m = board.size
        val n = board[0].size
        val tops = ArrayList<MutableList<Cell>>()
        for (i in 0 until m) {
            val row = ArrayList<Cell>()
            for (j in 0 until n) {
                val cur = Cell(board[i][j], j)
                var placed = false
                for (t in row.indices) {
                    if (cur.v > row[t].v) {
                        row.add(t, cur)
                        placed = true
                        break
                    }
                }
                if (!placed) row.add(cur)
                if (row.size > 3) row.subList(3, row.size).clear()
            }
            tops.add(row)
        }
        var ans = -(1L shl 62)
        for (i in 0 until m) {
            for (a in tops[i]) {
                for (j in i + 1 until m) {
                    for (b in tops[j]) {
                        if (a.c == b.c) continue
                        for (k in j + 1 until m) {
                            for (c in tops[k]) {
                                if (c.c == a.c || c.c == b.c) continue
                                val s = a.v.toLong() + b.v + c.v
                                if (s > ans) ans = s
                            }
                        }
                    }
                }
            }
        }
        return ans
    }
}
