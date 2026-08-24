// LeetCode 3380 - Maximum Area Rectangle With Point Constraints I
// https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i/

class Solution {
    fun maxRectangleArea(points: Array<IntArray>): Int {
        val set = HashSet<Long>()
        for (p in points) set.add(pack(p[0], p[1]))
        var ans = -1
        val n = points.size
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                val x1 = points[i][0]
                val y1 = points[i][1]
                val x2 = points[j][0]
                val y2 = points[j][1]
                if (x1 == x2 || y1 == y2) continue
                if (pack(x1, y2) !in set || pack(x2, y1) !in set) continue
                val minX = minOf(x1, x2)
                val maxX = maxOf(x1, x2)
                val minY = minOf(y1, y2)
                val maxY = maxOf(y1, y2)
                var ok = true
                for (p in points) {
                    val x = p[0]
                    val y = p[1]
                    if (x > minX && x < maxX && y > minY && y < maxY) {
                        ok = false
                        break
                    }
                    val onBorder = ((x == minX || x == maxX) && y in minY..maxY) ||
                        ((y == minY || y == maxY) && x in minX..maxX)
                    if (onBorder) {
                        val isCorner = (x == minX || x == maxX) && (y == minY || y == maxY)
                        if (!isCorner) {
                            ok = false
                            break
                        }
                    }
                }
                if (ok) {
                    val area = (maxX - minX) * (maxY - minY)
                    if (area > ans) ans = area
                }
            }
        }
        return ans
    }

    private fun pack(x: Int, y: Int): Long = (x.toLong() shl 32) xor (y.toLong() and 0xffffffffL)
}
