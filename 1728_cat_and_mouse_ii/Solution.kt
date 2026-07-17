// LeetCode 1728 - Cat and Mouse II
// https://leetcode.com/problems/cat-and-mouse-ii/

class Solution {
    fun canMouseWin(grid: Array<String>, catJump: Int, mouseJump: Int): Boolean {
        val rows = grid.size
        val cols = grid[0].length
        var totalOpen = 0
        var mouse = 0
        var cat = 0
        var food = 0
        for (r in 0 until rows) {
            for (c in 0 until cols) {
                val cell = grid[r][c]
                if (cell != '#') totalOpen++
                when (cell) {
                    'M' -> mouse = r * cols + c
                    'C' -> cat = r * cols + c
                    'F' -> food = r * cols + c
                }
            }
        }
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        fun computeMoves(pos: Int, jump: Int): IntArray {
            val r = pos / cols
            val c = pos % cols
            val out = ArrayList<Int>()
            out.add(pos)
            for (dir in dirs) {
                for (step in 1..jump) {
                    val nr = r + dir[0] * step
                    val nc = c + dir[1] * step
                    if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || grid[nr][nc] == '#') break
                    out.add(nr * cols + nc)
                }
            }
            return out.toIntArray()
        }
        val cells = rows * cols
        val mouseMoves = arrayOfNulls<IntArray>(cells)
        val catMoves = arrayOfNulls<IntArray>(cells)
        for (r in 0 until rows) {
            for (c in 0 until cols) {
                if (grid[r][c] != '#') {
                    val pos = r * cols + c
                    mouseMoves[pos] = computeMoves(pos, mouseJump)
                    catMoves[pos] = computeMoves(pos, catJump)
                }
            }
        }
        val maxTurn = 2 * totalOpen
        val memo = ByteArray(cells * cells * maxTurn)
        fun win(m: Int, c: Int, turn: Int): Boolean {
            if (turn >= maxTurn) return false
            if (m == food) return true
            if (c == food || c == m) return false
            val key = (m * cells + c) * maxTurn + turn
            if (memo[key] != 0.toByte()) return memo[key] == 1.toByte()
            var result: Boolean
            if (turn % 2 == 0) {
                result = false
                for (nm in mouseMoves[m]!!) {
                    if (win(nm, c, turn + 1)) {
                        result = true
                        break
                    }
                }
            } else {
                result = true
                for (nc in catMoves[c]!!) {
                    if (!win(m, nc, turn + 1)) {
                        result = false
                        break
                    }
                }
            }
            memo[key] = if (result) 1 else 2
            return result
        }
        return win(mouse, cat, 0)
    }
}
