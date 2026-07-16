// LeetCode 0544 - Output Contest Matches
// https://leetcode.com/problems/output-contest-matches/

class Solution {
    func findContestMatch(_ n: Int) -> String {
        var teams = (1...n).map { String($0) }
        while teams.count > 1 {
            var nextRound: [String] = []
            let half = teams.count / 2
            for i in 0..<half {
                nextRound.append("(\(teams[i]),\(teams[teams.count - 1 - i]))")
            }
            teams = nextRound
        }
        return teams[0]
    }
}
