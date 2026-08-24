// LeetCode 0469 - Convex Polygon
// https://leetcode.com/problems/convex-polygon/

class Solution {
    fun isConvex(points: Array<IntArray>): Boolean {
        var direction = 0
        val count = points.size
        for (index in 0 until count) {
            val x1 = points[(index + 1) % count][0] - points[index][0]
            val y1 = points[(index + 1) % count][1] - points[index][1]
            val x2 = points[(index + 2) % count][0] - points[(index + 1) % count][0]
            val y2 = points[(index + 2) % count][1] - points[(index + 1) % count][1]
            val cross = x1.toLong() * y2 - y1.toLong() * x2
            if (cross == 0L) {
                continue
            }
            val current = if (cross > 0) 1 else -1
            if (direction == 0) {
                direction = current
            } else if (direction != current) {
                return false
            }
        }
        return true
    }
}
