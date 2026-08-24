// LeetCode 3730 - Maximum Calories Burnt from Jumps
// https://leetcode.com/problems/maximum-calories-burnt-from-jumps/

class Solution {
    fun maxCaloriesBurnt(heights: IntArray): Long {
        heights.sort()
        var ans = 0
        var pre = 0
        var l = 0
        var r = heights.size - 1
        while (l < r) {
            var d1 = heights[r] - pre
            ans += d1 * d1
            var d2 = heights[l] - heights[r]
            ans += d2 * d2
            pre = heights[l]
            l = l + 1
            r = r - 1
        }
        var d = heights[r] - pre
        ans += d * d
        return ans
    }
}
