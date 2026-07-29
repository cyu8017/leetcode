// LeetCode 1036 - Escape a Large Maze
// https://leetcode.com/problems/escape-a-large-maze/

class Solution {
    fun isEscapePossible(blocked: Array<IntArray>, source: IntArray, target: IntArray): Boolean {
        val blockedSet = blocked.map { key(it[0], it[1]) }.toHashSet()
        val limit = blocked.size * (blocked.size - 1) / 2
        return bfs(source, target, blockedSet, limit) && bfs(target, source, blockedSet, limit)
    }

    private fun bfs(start: IntArray, goal: IntArray, blockedSet: Set<Long>, limit: Int): Boolean {
        val q = ArrayDeque<LongArray>()
        val seen = mutableSetOf<Long>()
        q.addLast(longArrayOf(start[0].toLong(), start[1].toLong()))
        seen.add(key(start[0], start[1]))
        val dirs = arrayOf(intArrayOf(1, 0), intArrayOf(-1, 0), intArrayOf(0, 1), intArrayOf(0, -1))
        while (q.isNotEmpty()) {
            if (seen.size > limit) return true
            val cur = q.removeFirst()
            val r = cur[0].toInt(); val c = cur[1].toInt()
            if (r == goal[0] && c == goal[1]) return true
            for (d in dirs) {
                val nr = r + d[0]; val nc = c + d[1]
                val k = key(nr, nc)
                if (nr in 0 until 1_000_000 && nc in 0 until 1_000_000 && k !in blockedSet && seen.add(k)) {
                    q.addLast(longArrayOf(nr.toLong(), nc.toLong()))
                }
            }
        }
        return false
    }

    private fun key(r: Int, c: Int) = (r.toLong() shl 32) or (c.toLong() and 0xffffffffL)
}
