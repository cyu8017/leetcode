// LeetCode 0800 - Similar RGB Color
// https://leetcode.com/problems/similar-rgb-color/

class Solution {
    fun similarRGB(color: String): String {
        return "#" + closest(color.substring(1, 3)) + closest(color.substring(3, 5))
            + closest(color.substring(5, 7))
    }

    private fun closest(component: String): String {
        var value = component, 16.toInt()
        var rounded = (value + 8) / 17
        return String.format("%x%x", rounded, rounded)
    }
}
