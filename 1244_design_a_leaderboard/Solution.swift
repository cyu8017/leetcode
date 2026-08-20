// LeetCode 1244 - Design A Leaderboard
// https://leetcode.com/problems/design-a-leaderboard/

class Leaderboard {
    private var scores: [Int: Int] = [:]

    func addScore(_ playerId: Int, _ score: Int) {
        scores[playerId, default: 0] += score
    }

    func top(_ K: Int) -> Int {
        Array(scores.values).sorted(by: >).prefix(K).reduce(0, +)
    }

    func reset(_ playerId: Int) {
        scores[playerId] = nil
    }
}
