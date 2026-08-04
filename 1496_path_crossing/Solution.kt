// LeetCode 1496 - Path Crossing
// https://leetcode.com/problems/path-crossing/

class Solution {
    fun isPathCrossing(path: String): Boolean {
        var x = 0
        var y = 0
        val seen = HashSet<Long>()
        seen.add(0L)
        val move = mapOf('N' to (0 to 1), 'S' to (0 to -1), 'E' to (1 to 0), 'W' to (-1 to 0))
        for (c in path) {
            val (dx, dy) = move[c]!!
            x += dx
            y += dy
            val key = (x.toLong() shl 32) or (y.toLong() and 0xffffffffL)
            if (!seen.add(key)) return true
        }
        return false
    }
}
