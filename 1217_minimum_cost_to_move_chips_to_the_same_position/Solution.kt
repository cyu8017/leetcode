// LeetCode 1217 - Minimum Cost to Move Chips to The Same Position
// https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

class Solution {
    fun minCostToMoveChips(position: IntArray): Int {
        var odd = 0
        for (x in position) if (x and 1 == 1) odd++
        return minOf(odd, position.size - odd)
    }
}
