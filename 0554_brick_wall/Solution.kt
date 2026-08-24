// LeetCode 0554 - Brick Wall
// https://leetcode.com/problems/brick-wall/


class Solution {
    fun leastBricks(wall: List<List<Int>>): Int {
        val edges = HashMap<Int, Int>()
        var best = 0
        for (row in wall) {
            var width = 0
            for (i in 0 until row.size - 1) {
                width += row[i]
                val count = edges.getOrDefault(width, 0) + 1
                edges[width] = count
                best = maxOf(best, count)
            }
        }
        return wall.size - best
    }
}
