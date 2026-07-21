// LeetCode 1872 - Stone Game VIII
// https://leetcode.com/problems/stone-game-viii/

class Solution {
    func stoneGameVIII(_ stones: [Int]) -> Int {
        var stones = stones
        let n = stones.count
        for i in 1..<n {
            stones[i] += stones[i - 1]
        }

        var score = stones[n - 1]
        if n <= 1 {
            return score
        }
        for i in stride(from: n - 2, through: 1, by: -1) {
            score = max(stones[i] - score, score)
        }
        return score
    }
}
