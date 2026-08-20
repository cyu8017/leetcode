// LeetCode 1335 - Minimum Difficulty of a Job Schedule
// https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

class Solution {
    func minDifficulty(_ jobDifficulty: [Int], _ d: Int) -> Int {
        let n = jobDifficulty.count
        if n < d { return -1 }
        var dp = Array(repeating: Int.max / 4, count: n)
        var hardest = 0
        for i in 0..<n {
            hardest = max(hardest, jobDifficulty[i])
            dp[i] = hardest
        }
        for day in 1..<d {
            var nxt = Array(repeating: Int.max / 4, count: n)
            for end in day..<n {
                hardest = 0
                for start in stride(from: end, through: day, by: -1) {
                    hardest = max(hardest, jobDifficulty[start])
                    nxt[end] = min(nxt[end], dp[start - 1] + hardest)
                }
            }
            dp = nxt
        }
        return dp[n - 1]
    }
}
