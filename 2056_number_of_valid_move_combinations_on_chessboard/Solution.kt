// LeetCode 2056 - Number of Valid Move Combinations On Chessboard
// https://leetcode.com/problems/number-of-valid-move-combinations-on-chessboard/

class Solution {
    private class Move(val dr: Int, val dc: Int, val steps: Int)

    private lateinit var pieces: Array<String>
    private lateinit var positions: Array<IntArray>
    private lateinit var allMoves: Array<MutableList<Move>>
    private lateinit var chosen: Array<Move?>
    private var ans = 0

    fun countCombinations(pieces: Array<String>, positions: Array<IntArray>): Int {
        this.pieces = pieces
        this.positions = positions
        val dirs = HashMap<String, Array<IntArray>>()
        dirs["rook"] = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        dirs["bishop"] = arrayOf(intArrayOf(1, 1), intArrayOf(1, -1), intArrayOf(-1, 1), intArrayOf(-1, -1))
        dirs["queen"] = arrayOf(
            intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1),
            intArrayOf(1, 1), intArrayOf(1, -1), intArrayOf(-1, 1), intArrayOf(-1, -1)
        )
        val n = pieces.size
        allMoves = Array(n) { mutableListOf() }
        for (i in 0 until n) {
            val ms = mutableListOf<Move>()
            ms.add(Move(0, 0, 0))
            val r = positions[i][0]
            val c = positions[i][1]
            for (d in dirs[pieces[i]]!!) {
                var nr = r + d[0]
                var nc = c + d[1]
                var step = 1
                while (nr in 1..8 && nc in 1..8) {
                    ms.add(Move(d[0], d[1], step))
                    nr += d[0]
                    nc += d[1]
                    step++
                }
            }
            allMoves[i] = ms
        }
        chosen = arrayOfNulls(n)
        ans = 0
        dfs(0)
        return ans
    }

    private fun okCombo(end: Int): Boolean {
        var maxT = 0
        for (i in 0..end) maxT = maxOf(maxT, chosen[i]!!.steps)
        for (t in 1..maxT) {
            val seen = HashSet<Long>()
            for (i in 0..end) {
                val m = chosen[i]!!
                val pr: Int
                val pc: Int
                if (m.steps == 0) {
                    pr = positions[i][0]
                    pc = positions[i][1]
                } else {
                    val use = minOf(t, m.steps)
                    pr = positions[i][0] + m.dr * use
                    pc = positions[i][1] + m.dc * use
                }
                val key = (pr.toLong() shl 32) xor (pc.toLong() and 0xffffffffL)
                if (!seen.add(key)) return false
            }
        }
        return true
    }

    private fun dfs(i: Int) {
        if (i == pieces.size) {
            ans++
            return
        }
        for (m in allMoves[i]) {
            chosen[i] = m
            if (okCombo(i)) dfs(i + 1)
        }
    }
}
