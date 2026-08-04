// LeetCode 1210 - Minimum Moves to Reach Target With Rotations
// https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/

class Solution {
    fun minimumMoves(grid: Array<IntArray>): Int {
        val n = grid.size
        val queue = ArrayDeque<IntArray>()
        queue.add(intArrayOf(0, 0, 0, 0))
        val seen = mutableSetOf("0,0,0")
        while (queue.isNotEmpty()) {
            val cur = queue.removeFirst()
            val r = cur[0]
            val c = cur[1]
            val orient = cur[2]
            val moves = cur[3]
            if (r == n - 1 && c == n - 2 && orient == 0) return moves
            val next = mutableListOf<IntArray>()
            if (orient == 0) {
                if (c + 2 < n && grid[r][c + 2] == 0) next.add(intArrayOf(r, c + 1, 0))
                if (r + 1 < n && grid[r + 1][c] == 0 && grid[r + 1][c + 1] == 0) {
                    next.add(intArrayOf(r + 1, c, 0))
                    next.add(intArrayOf(r, c, 1))
                }
            } else {
                if (r + 2 < n && grid[r + 2][c] == 0) next.add(intArrayOf(r + 1, c, 1))
                if (c + 1 < n && grid[r][c + 1] == 0 && grid[r + 1][c + 1] == 0) {
                    next.add(intArrayOf(r, c + 1, 1))
                    next.add(intArrayOf(r, c, 0))
                }
            }
            for (state in next) {
                val key = "${state[0]},${state[1]},${state[2]}"
                if (seen.add(key)) queue.add(intArrayOf(state[0], state[1], state[2], moves + 1))
            }
        }
        return -1
    }
}
