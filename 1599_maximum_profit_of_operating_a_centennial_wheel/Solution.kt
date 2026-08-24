// LeetCode 1599 - Maximum Profit of Operating a Centennial Wheel
// https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/

class Solution {
    fun minOperationsMaxProfit(customers: IntArray, boardingCost: Int, runningCost: Int): Int {
        var waiting = 0
        var profit = 0
        var best = 0
        var answer = 0
        var rotation = 0
        var i = 0
        while (i < customers.size || waiting > 0) {
            if (i < customers.size) waiting += customers[i]
            val boarded = minOf(4, waiting)
            waiting -= boarded
            rotation++
            profit += boarded * boardingCost - runningCost
            if (profit > best) {
                best = profit
                answer = rotation
            }
            i++
        }
        return if (best > 0) answer else -1
    }
}
