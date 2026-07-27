// LeetCode 1626 - Best Team With No Conflicts
// https://leetcode.com/problems/best-team-with-no-conflicts/

class Solution {
    func bestTeamScore(_ scores: [Int], _ ages: [Int]) -> Int {
        let players = zip(ages, scores).sorted { $0.0 == $1.0 ? $0.1 < $1.1 : $0.0 < $1.0 }
        var dp = [Int](repeating: 0, count: players.count)
        for i in 0..<players.count {
            let score = players[i].1
            var best = 0
            for j in 0..<i where players[j].1 <= score {
                best = max(best, dp[j])
            }
            dp[i] = score + best
        }
        return dp.max() ?? 0
    }
}
