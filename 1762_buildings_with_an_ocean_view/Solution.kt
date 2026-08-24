// LeetCode 1762 - Buildings With an Ocean View
// https://leetcode.com/problems/buildings-with-an-ocean-view/

class Solution {
    fun findBuildings(heights: IntArray): IntArray {
        val ans = mutableListOf<Int>()
        var tallest = 0
        for (i in heights.indices.reversed()) {
            if (heights[i] > tallest) {
                ans.add(i)
                tallest = heights[i]
            }
        }
        ans.reverse()
        return ans.toIntArray()
    }
}
