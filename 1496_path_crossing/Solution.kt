// LeetCode 1496 - Path Crossing
// https://leetcode.com/problems/path-crossing/

class Solution {
    fun isPathCrossing(path: String): Boolean {
        var x = 0
        var y = 0
        val seen = mutableSetOf(0 to 0)
        val move = mapOf('N' to (0 to 1), 'S' to (0 to -1), 'E' to (1 to 0), 'W' to (-1 to 0))
        for (c in path) {
            val (dx, dy) = move[c]!!
            x += dx
            y += dy
            if (x to y in seen) return true
            seen.add(x to y)
        }
        return false
    }
}
