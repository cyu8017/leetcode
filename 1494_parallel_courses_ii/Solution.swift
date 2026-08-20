// LeetCode 1494 - Parallel Courses II
// https://leetcode.com/problems/parallel-courses-ii/

class Solution {
    func minNumberOfSemesters(_ n: Int, _ relations: [[Int]], _ k: Int) -> Int {
        var prereq = Array(repeating: 0, count: n)
        for e in relations { prereq[e[1] - 1] |= 1 << (e[0] - 1) }
        let full = (1 << n) - 1, inf = Int.max / 4
        var dp = Array(repeating: inf, count: 1 << n)
        dp[0] = 0
        for mask in 0..<(1 << n) where dp[mask] != inf {
            var available = 0
            for c in 0..<n where mask & (1 << c) == 0 && (prereq[c] & mask) == prereq[c] {
                available |= 1 << c
            }
            var choices = [Int]()
            if available.nonzeroBitCount <= k {
                choices = [available]
            } else {
                var sub = available
                while sub > 0 {
                    if sub.nonzeroBitCount == k { choices.append(sub) }
                    sub = (sub - 1) & available
                }
            }
            for take in choices {
                dp[mask | take] = min(dp[mask | take], dp[mask] + 1)
            }
        }
        return dp[full]
    }
}
