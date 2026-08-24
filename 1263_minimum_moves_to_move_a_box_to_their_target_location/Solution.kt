// LeetCode 1263 - Minimum Moves to Move a Box to Their Target Location
// https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/

class Solution {
    fun minPushBox(grid: Array<CharArray>): Int {
        val m = grid.size
        val n = grid[0].size
        var br = 0; var bc = 0; var pr = 0; var pc = 0; var tr = 0; var tc = 0
        for (r in 0 until m) {
            for (c in 0 until n) {
                when (grid[r][c]) {
                    'B' -> { br = r; bc = c }
                    'S' -> { pr = r; pc = c }
                    'T' -> { tr = r; tc = c }
                }
            }
        }
        val queue = ArrayDeque<IntArray>()
        val seen = mutableSetOf<Long>()
        queue.add(intArrayOf(br, bc, pr, pc, 0))
        seen.add(stateKey(br, bc, pr, pc, n))
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        while (queue.isNotEmpty()) {
            val cur = queue.removeFirst()
            val boxR = cur[0]; val boxC = cur[1]; val playerR = cur[2]; val playerC = cur[3]; val pushes = cur[4]
            if (boxR == tr && boxC == tc) return pushes
            val canReach = reachable(grid, m, n, playerR, playerC, boxR, boxC)
            for (d in dirs) {
                val sr = boxR - d[0]; val sc = boxC - d[1]
                val nbr = boxR + d[0]; val nbc = boxC + d[1]
                if (sr * n + sc !in canReach) continue
                if (nbr !in 0 until m || nbc !in 0 until n || grid[nbr][nbc] == '#') continue
                val key = stateKey(nbr, nbc, boxR, boxC, n)
                if (seen.add(key)) queue.add(intArrayOf(nbr, nbc, boxR, boxC, pushes + 1))
            }
        }
        return -1
    }

    private fun stateKey(br: Int, bc: Int, pr: Int, pc: Int, n: Int): Long =
        ((br.toLong() * n + bc) shl 20) or (pr * n + pc).toLong()

    private fun reachable(grid: Array<CharArray>, m: Int, n: Int, pr: Int, pc: Int, br: Int, bc: Int): Set<Int> {
        val seen = mutableSetOf(pr * n + pc)
        val stack = ArrayDeque<IntArray>()
        stack.addLast(intArrayOf(pr, pc))
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        while (stack.isNotEmpty()) {
            val cur = stack.removeLast()
            for (d in dirs) {
                val nr = cur[0] + d[0]; val nc = cur[1] + d[1]
                val key = nr * n + nc
                if (nr !in 0 until m || nc !in 0 until n || grid[nr][nc] == '#') continue
                if (nr == br && nc == bc) continue
                if (seen.add(key)) stack.addLast(intArrayOf(nr, nc))
            }
        }
        return seen
    }
}
