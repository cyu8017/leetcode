// LeetCode 2140 - Solving Questions With Brainpower
// https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution {
    func mostPoints(_ questions: [[Int]]) -> Int {
        let n = questions.count
        var dp = [Int](repeating: 0, count: n + 1)
        for i in stride(from: n - 1, through: 0, by: -1) {
            let pts = questions[i][0], brain = questions[i][1]
            let next = i + brain + 1
            let take = pts + (next < n ? dp[next] : 0)
            dp[i] = max(dp[i + 1], take)
        }
        return dp[0]
    }
}
