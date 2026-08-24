// LeetCode 2848 - Points That Intersect With Cars
// https://leetcode.com/problems/points-that-intersect-with-cars/


class Solution {
    fun numberOfPoints(nums: List<List<Int>>): Int {
        val cov = IntArray(102)
        for (r in nums) {
            for (x in r[0]..r[1]) cov[x] = 1
        }
        var ans = 0
        for (v in cov) ans += v
        return ans
    }
}
