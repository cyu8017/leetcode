// LeetCode 3740 - Minimum Distance Between Three Equal Elements I
// https://leetcode.com/problems/minimum_distance_between_three_equal_elements_i/

class Solution {
    fun minimumDistance(nums: IntArray): Int {
        var g = HashMap<Int, MutableList<Int>>()
        for (i in 0 until nums.size) {
            g.getOrPut(nums[i]) { ArrayList() }.add(i)
        }
        var inf = 1  shl  30
        var ans = inf
        for (ls in g.values) {
            var m = ls.size
            for (h in 0 until m - 2) {
                ans = minOf(ans, (ls[h + 2] - ls[h]) * 2)
            }
        }
        return if (ans == inf) -1 else ans
    }
}
