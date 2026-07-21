// LeetCode 1828 - Queries on Number of Points Inside a Circle
// https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

class Solution {
    fun countPoints(points: Array<IntArray>, queries: Array<IntArray>): IntArray {
        return IntArray(queries.size) { qi ->
            val xq = queries[qi][0]
            val yq = queries[qi][1]
            val r = queries[qi][2]
            val radiusSq = r * r
            var count = 0
            for (p in points) {
                val dx = p[0] - xq
                val dy = p[1] - yq
                if (dx * dx + dy * dy <= radiusSq) count++
            }
            count
        }
    }
}
