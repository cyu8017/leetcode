// LeetCode 0506 - Relative Ranks
// https://leetcode.com/problems/relative-ranks/

class Solution {
    func findRelativeRanks(_ score: [Int]) -> [String] {
        let medals: [Int: String] = [
            1: "Gold Medal",
            2: "Silver Medal",
            3: "Bronze Medal",
        ]
        let order = (0..<score.count).sorted { score[$0] > score[$1] }
        var result = Array(repeating: "", count: score.count)
        for (rank, index) in order.enumerated() {
            result[index] = medals[rank + 1] ?? String(rank + 1)
        }
        return result
    }
}
