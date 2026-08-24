// LeetCode 0672 - Bulb Switcher II
// https://leetcode.com/problems/bulb-switcher-ii/


class Solution {
    fun flipLights(n: Int, presses: Int): Int {
        val m = minOf(n, 3)
        if (presses == 0) return 1
        if (m == 1) return 2
        if (m == 2) return if (presses == 1) 3 else 4
        return when (presses) {
            1 -> 4
            2 -> 7
            else -> 8
        }
    }
}
