// LeetCode 3027 - Find the Number of Ways to Place People II
// https://leetcode.com/problems/find-the-number-of-ways-to-place-people-ii/

class Solution {
    fun numberOfPairs(points: Array<IntArray>): Int {
        points.sortWith(compareBy<IntArray> { it[0] }.thenByDescending { it[1] })
        var ans = 0
        for (i in points.indices) {
            val y1 = points[i][1]
            var maxY = Int.MIN_VALUE
            for (j in i + 1 until points.size) {
                val y2 = points[j][1]
                if (maxY < y2 && y2 <= y1) {
                    maxY = y2
                    ans++
                }
            }
        }
        return ans
    }
}
