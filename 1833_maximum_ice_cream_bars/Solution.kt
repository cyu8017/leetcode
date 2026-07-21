// LeetCode 1833 - Maximum Ice Cream Bars
// https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution {
    fun maxIceCream(costs: IntArray, coins: Int): Int {
        costs.sort()
        var remaining = coins
        var count = 0
        for (cost in costs) {
            if (remaining < cost) break
            remaining -= cost
            count++
        }
        return count
    }
}
