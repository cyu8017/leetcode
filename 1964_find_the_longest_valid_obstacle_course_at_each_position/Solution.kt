// LeetCode 1964
// https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

class Solution {
    fun longestObstacleCourseAtEachPosition(obstacles: IntArray): IntArray {
        val tails = mutableListOf<Int>()
        val ans = IntArray(obstacles.size)
        for (i in obstacles.indices) {
            val x = obstacles[i]
            var lo = 0
            var hi = tails.size
            while (lo < hi) {
                val mid = (lo + hi) / 2
                if (tails[mid] <= x) lo = mid + 1 else hi = mid
            }
            if (lo == tails.size) tails.add(x) else tails[lo] = x
            ans[i] = lo + 1
        }
        return ans
    }
}
