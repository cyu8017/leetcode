// LeetCode 1833 - Maximum Ice Cream Bars
// https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution {
    func maxIceCream(_ costs: [Int], _ coins: Int) -> Int {
        var remaining = coins
        var count = 0
        for cost in costs.sorted() {
            if remaining < cost { break }
            remaining -= cost
            count += 1
        }
        return count
    }
}
