// LeetCode 3332 - Maximum Points Tourist Can Earn
// https://leetcode.com/problems/maximum-points-tourist-can-earn/

class Solution {
    func maxScore(_ n: Int, _ k: Int, _ stayScore: [[Int]], _ travelScore: [[Int]]) -> Int {
        var dp = Array(repeating: 0, count: n)
        for day in 0..<k {
            var ndp = Array(repeating: -(1 << 30), count: n)
            for dest in 0..<n {
                var best = -(1 << 30)
                for src in 0..<n {
                    var val = dp[src]
                    if src == dest { val += stayScore[day][dest] }
                    else { val += travelScore[src][dest] }
                    if val > best { best = val }
                }
                ndp[dest] = best
            }
            dp = ndp
        }
        return dp.max() ?? 0
    }
}
