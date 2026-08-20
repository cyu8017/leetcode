// LeetCode 1986 - Minimum Number of Work Sessions to Finish the Tasks
// https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/

class Solution {
    func minSessions(_ tasks: [Int], _ sessionTime: Int) -> Int {
        let n = tasks.count
        let INF = (n + 1, 0)
        var dp = Array(repeating: INF, count: 1 << n)
        dp[0] = (1, 0)
        for mask in 0..<(1 << n) {
            let (sessions, used) = dp[mask]
            if sessions > n { continue }
            for i in 0..<n where mask & (1 << i) == 0 {
                let t = tasks[i]
                let nmask = mask | (1 << i)
                let cand: (Int, Int) = used + t <= sessionTime ? (sessions, used + t) : (sessions + 1, t)
                if cand < dp[nmask] { dp[nmask] = cand }
            }
        }
        return dp[(1 << n) - 1].0
    }
}
