// LeetCode 3225 - Maximum Score From Grid Operations
// https://leetcode.com/problems/maximum-score-from-grid-operations/

class Solution {
    func maximumScore(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var prefix = Array(repeating: Array(repeating: 0, count: n + 1), count: n)
        for j in 0..<n {
            for i in 0..<n { prefix[j][i + 1] = prefix[j][i] + grid[i][j] }
        }
        var prevPick = Array(repeating: 0, count: n + 1)
        var prevSkip = Array(repeating: 0, count: n + 1)
        if n >= 2 {
            for j in 1..<n {
                var currPick = Array(repeating: 0, count: n + 1)
                var currSkip = Array(repeating: 0, count: n + 1)
                for curr in 0...n {
                    for prev in 0...n {
                        if curr > prev {
                            let score = prefix[j - 1][curr] - prefix[j - 1][prev]
                            currPick[curr] = max(currPick[curr], prevSkip[prev] + score)
                            currSkip[curr] = max(currSkip[curr], prevSkip[prev] + score)
                        } else {
                            let score = prefix[j][prev] - prefix[j][curr]
                            currPick[curr] = max(currPick[curr], prevPick[prev] + score)
                            currSkip[curr] = max(currSkip[curr], prevPick[prev])
                        }
                    }
                }
                prevPick = currPick
                prevSkip = currSkip
            }
        }
        return prevPick.max()!
    }
}
