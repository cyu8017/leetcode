// LeetCode 3522 - Calculate Score After Performing Instructions
// https://leetcode.com/problems/calculate-score-after-performing-instructions/

class Solution {
    func calculateScore(_ instructions: [String], _ values: [Int]) -> Int {
        let n = values.count
        var vis = Array(repeating: false, count: n)
        var ans = 0
        var i = 0
        while i >= 0 && i < n && !vis[i] {
            vis[i] = true
            if instructions[i].first == "a" {
                ans += values[i]
                i += 1
            } else {
                i += values[i]
            }
        }
        return ans
    }
}
