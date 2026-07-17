// LeetCode 1753 - Maximum Score From Removing Stones
// https://leetcode.com/problems/maximum-score-from-removing-stones/

class Solution {
    func maximumScore(_ a: Int, _ b: Int, _ c: Int) -> Int {
        var stones = [a, b, c].sorted(by: >)
        var score = 0
        while stones[0] > 0 && stones[1] > 0 {
            stones[0] -= 1
            stones[1] -= 1
            score += 1
            stones.sort(by: >)
        }
        return score
    }
}
