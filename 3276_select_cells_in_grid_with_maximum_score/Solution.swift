// LeetCode 3276 - Select Cells in Grid With Maximum Score
// https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/

class Solution {
    func maxScore(_ grid: [[Int]]) -> Int {
        let m = grid.count
        var vals: [Int: [Int]] = [:]
        for i in 0..<m {
            var seen = Set<Int>()
            for v in grid[i] where seen.insert(v).inserted {
                vals[v, default: []].append(i)
            }
        }
        let arr = vals.keys.sorted(by: >)
        let N = 1 << m
        var dp = Array(repeating: 0, count: N)
        for v in arr {
            var ndp = dp
            for r in vals[v]! {
                let bit = 1 << r
                for mask in 0..<N where (mask & bit) == 0 {
                    let cand = dp[mask] + v
                    let nmask = mask | bit
                    if cand > ndp[nmask] { ndp[nmask] = cand }
                }
            }
            dp = ndp
        }
        return dp.max()!
    }
}
