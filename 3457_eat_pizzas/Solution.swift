// LeetCode 3457 - Eat Pizzas!
// https://leetcode.com/problems/eat-pizzas/

class Solution {
    func maxWeight(_ pizzas: [Int]) -> Int {
        let pizzas = pizzas.sorted()
        let n = pizzas.count
        let days = n / 4
        var ans = 0
        let oddDays = (days + 1) / 2
        let evenDays = days / 2
        var idx = n - 1
        for _ in 0..<oddDays {
            ans += pizzas[idx]
            idx -= 1
        }
        for _ in 0..<evenDays {
            idx -= 1
            ans += pizzas[idx]
            idx -= 1
        }
        return ans
    }
}
