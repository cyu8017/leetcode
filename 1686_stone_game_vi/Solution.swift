// LeetCode 1686 - Stone Game VI
// https://leetcode.com/problems/stone-game-vi/

class Solution {
    func stoneGameVI(_ aliceValues: [Int], _ bobValues: [Int]) -> Int {
        let order = (0..<aliceValues.count).sorted {
            (aliceValues[$0] + bobValues[$0]) > (aliceValues[$1] + bobValues[$1])
        }
        var score = 0
        for (t, i) in order.enumerated() {
            score += t % 2 == 0 ? aliceValues[i] : -bobValues[i]
        }
        return score > 0 ? 1 : (score < 0 ? -1 : 0)
    }
}
