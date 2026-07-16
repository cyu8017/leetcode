// LeetCode 0495 - Teemo Attacking
// https://leetcode.com/problems/teemo-attacking/

class Solution {
    func findPoisonedDuration(_ timeSeries: [Int], _ duration: Int) -> Int {
        if timeSeries.isEmpty {
            return 0
        }
        var total = duration
        if timeSeries.count > 1 {
            for index in 1..<timeSeries.count {
                total += min(duration, timeSeries[index] - timeSeries[index - 1])
            }
        }
        return total
    }
}
