// LeetCode 1956
// https://leetcode.com/problems/minimum-time-for-k-virus-variants-to-spread/

class Solution {
    fun minDayskVariants(points: Array<IntArray>, k: Int): Int {
        var ans = Int.MAX_VALUE
        for (x in 1..100) for (y in 1..100) {
            val dists = points.map { kotlin.math.abs(it[0] - x) + kotlin.math.abs(it[1] - y) }.sorted()
            ans = minOf(ans, dists[k - 1])
        }
        return ans
    }
}
