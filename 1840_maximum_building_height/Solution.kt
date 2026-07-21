// LeetCode 1840 - Maximum Building Height
// https://leetcode.com/problems/maximum-building-height/

class Solution {
    fun maxBuilding(n: Int, restrictions: Array<IntArray>): Int {
        val points = ArrayList<IntArray>()
        points.add(intArrayOf(1, 0))
        restrictions.sortedBy { it[0] }.forEach { points.add(intArrayOf(it[0], it[1])) }
        if (points.last()[0] != n) points.add(intArrayOf(n, n - 1))

        for (i in 1 until points.size) {
            val prevId = points[i - 1][0]
            val prevHeight = points[i - 1][1]
            val currId = points[i][0]
            val currHeight = points[i][1]
            points[i][1] = minOf(currHeight, prevHeight + currId - prevId)
        }

        for (i in points.size - 2 downTo 0) {
            val nextId = points[i + 1][0]
            val nextHeight = points[i + 1][1]
            val currId = points[i][0]
            val currHeight = points[i][1]
            points[i][1] = minOf(currHeight, nextHeight + nextId - currId)
        }

        var best = points.maxOf { it[1] }
        for (i in 0 until points.size - 1) {
            val id1 = points[i][0]
            val h1 = points[i][1]
            val id2 = points[i + 1][0]
            val h2 = points[i + 1][1]
            best = maxOf(best, (h1 + h2 + id2 - id1) / 2)
        }
        return best
    }
}
