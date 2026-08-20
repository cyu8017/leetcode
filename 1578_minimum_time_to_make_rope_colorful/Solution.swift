// LeetCode 1578 - Minimum Time to Make Rope Colorful
// https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

class Solution {
    func minCost(_ colors: String, _ neededTime: [Int]) -> Int {
        let cols = Array(colors)
        var answer = 0, maximum = 0
        for (i, cost) in neededTime.enumerated() {
            if i > 0 && cols[i] != cols[i - 1] { maximum = 0 }
            answer += min(maximum, cost)
            maximum = max(maximum, cost)
        }
        return answer
    }
}
