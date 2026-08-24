// LeetCode 1274 - Number of Ships in a Rectangle
// https://leetcode.com/problems/number-of-ships-in-a-rectangle/

interface Sea {
    fun hasShips(topRight: IntArray, bottomLeft: IntArray): Boolean
}

class Solution {
    fun countShips(sea: Sea, topRight: IntArray, bottomLeft: IntArray): Int {
        val tx = topRight[0]
        val ty = topRight[1]
        val bx = bottomLeft[0]
        val by = bottomLeft[1]
        if (tx < bx || ty < by || !sea.hasShips(topRight, bottomLeft)) return 0
        if (tx == bx && ty == by) return 1
        val mx = (tx + bx) / 2
        val my = (ty + by) / 2
        return countShips(sea, intArrayOf(mx, my), bottomLeft) +
            countShips(sea, intArrayOf(tx, my), intArrayOf(mx + 1, by)) +
            countShips(sea, intArrayOf(mx, ty), intArrayOf(bx, my + 1)) +
            countShips(sea, topRight, intArrayOf(mx + 1, my + 1))
    }
}
