// LeetCode 3594 - Minimum Time to Transport All Individuals
// https://leetcode.com/problems/minimum-time-to-transport-all-individuals/

class Solution {
    func minTime(_ n: Int, _ k: Int, _ m: Int, _ time: [Int], _ mul: [Double]) -> Double {
        var t = time.sorted()
        var total = 0.0
        var stage = 0, left = n
        while left > 0 {
            let take = min(k, left)
            let slow = t[left - 1]
            total += Double(slow) * mul[stage % m]
            left -= take
            stage += 1
            if left > 0 {
                total += Double(t[0]) * mul[stage % m]
                stage += 1
            }
        }
        return total
    }
}
