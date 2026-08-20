// LeetCode 1366 - Rank Teams by Votes
// https://leetcode.com/problems/rank-teams-by-votes/

class Solution {
    func rankTeams(_ votes: [String]) -> String {
        let m = votes[0].count
        var count = [Character: [Int]]()
        for c in votes[0] { count[c] = Array(repeating: 0, count: m) }
        for v in votes {
            for (i, c) in Array(v).enumerated() { count[c]![i] += 1 }
        }
        return String(count.keys.sorted { a, b in
            for i in 0..<m {
                if count[a]![i] != count[b]![i] { return count[a]![i] > count[b]![i] }
            }
            return a < b
        })
    }
}
