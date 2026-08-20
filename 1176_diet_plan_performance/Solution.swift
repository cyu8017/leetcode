// LeetCode 1176 - Diet Plan Performance
// https://leetcode.com/problems/diet-plan-performance/

class Solution {
    func dietPlanPerformance(_ calories: [Int], _ k: Int, _ lower: Int, _ upper: Int) -> Int {
        var window = calories.prefix(k).reduce(0, +)
        var points = 0
        if window < lower { points -= 1 }
        else if window > upper { points += 1 }
        for i in k..<calories.count {
            window += calories[i] - calories[i - k]
            if window < lower { points -= 1 }
            else if window > upper { points += 1 }
        }
        return points
    }
}
