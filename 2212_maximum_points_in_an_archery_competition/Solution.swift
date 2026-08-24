// LeetCode 2212 - Maximum Points in an Archery Competition
// https://leetcode.com/problems/maximum-points-in-an-archery-competition/

class Solution {
    func maximumBobPoints(_ numArrows: Int, _ aliceArrows: [Int]) -> [Int] {
        var bestScore = -1
        var best = [Int](repeating: 0, count: 12)
        var bob = [Int](repeating: 0, count: 12)
        func dfs(_ i: Int, _ remain: Int, _ score: Int) {
            if i == 12 {
                if score > bestScore {
                    bestScore = score
                    best = bob
                    if remain > 0 { best[0] += remain }
                }
                return
            }
            dfs(i + 1, remain, score)
            let need = aliceArrows[i] + 1
            if remain >= need {
                bob[i] = need
                dfs(i + 1, remain - need, score + i)
                bob[i] = 0
            }
        }
        dfs(0, numArrows, 0)
        return best
    }
}
