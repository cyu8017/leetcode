// LeetCode 1936
// https://leetcode.com/problems/add-minimum-number-of-rungs/

class Solution {
    fun addRungs(rungs: IntArray, dist: Int): Int {
        var prev = 0
        var ans = 0
        for (r in rungs) {
            val gap = r - prev
            if (gap > dist) ans += (gap - 1) / dist
            prev = r
        }
        return ans
    }
}
