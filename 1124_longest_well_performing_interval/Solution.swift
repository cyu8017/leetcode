// LeetCode 1124 - Longest Well-Performing Interval
// https://leetcode.com/problems/longest-well-performing-interval/

class Solution {
    func longestWPI(_ hours: [Int]) -> Int {
        var score = 0, ans = 0
        var firstSeen: [Int: Int] = [0: -1]
        for i in 0..<hours.count {
            score += hours[i] > 8 ? 1 : -1
            if score > 0 {
                ans = i + 1
            } else if let prev = firstSeen[score - 1] {
                ans = max(ans, i - prev)
            }
            if firstSeen[score] == nil { firstSeen[score] = i }
        }
        return ans
    }
}
