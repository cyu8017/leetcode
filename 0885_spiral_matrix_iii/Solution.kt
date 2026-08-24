// LeetCode 0885 - Spiral Matrix III
// https://leetcode.com/problems/spiral-matrix-iii/

class Solution {
    fun spiralMatrixIII(rows: Int, cols: Int, rStart: Int, cStart: Int): Array<IntArray> {
        var ans = mutableListOf()
        ans.add(intArrayOf(rStart, cStart))
        if (rows * cols == 1) return ans.toArray(IntArray(0)[])
        var r = rStart
        var c = cStart
        var dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
        var steps = 1
        while (ans.size < rows * cols) {
            for (d in 0 until 4) {
                var dr = dirs[d][0]
                var dc = dirs[d][1]
                for (i in 0 until steps) {
                    r += dr
                    c += dc
                    if (r >= 0 && r < rows && c >= 0 && c < cols) {
                        ans.add(intArrayOf(r, c))
                        if (ans.size == rows * cols) return ans.toArray(IntArray(0)[])
                    }
                }
                if (d % 2 == 1) steps++
            }
        }
        return ans.toArray(IntArray(0)[])
    }
}
