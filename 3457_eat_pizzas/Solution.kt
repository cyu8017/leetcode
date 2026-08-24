// LeetCode 3457 - Eat Pizzas!
// https://leetcode.com/problems/eat-pizzas/

class Solution {
    fun maxWeight(pizzas: IntArray): Long {
        pizzas.sort()
        var n = pizzas.size
        var days = n / 4
        var ans = 0
        var oddDays = (days + 1) / 2
        var evenDays = days / 2
        var idx = n - 1
        for (i in 0 until oddDays) {
            ans += pizzas[idx]
            idx = idx - 1
        }
        for (i in 0 until evenDays) {
            idx = idx - 1
            ans += pizzas[idx]
            idx = idx - 1
        }
        return ans
    }
}
