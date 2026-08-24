// LeetCode 3888 - Minimum Operations To Make All Grid Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-grid-elements-equal/

class Solution {
    private var grid = [[Int]]()
    private var k = 0, m = 0, n = 0

    func minOperations(_ grid: [[Int]], _ k: Int) -> Int {
        self.grid = grid
        self.k = k
        m = grid.count
        n = grid[0].count
        var maxVal = grid[0][0]
        for row in grid {
            for x in row { maxVal = max(maxVal, x) }
        }
        for t in maxVal...(maxVal + 1) {
            let res = check(t)
            if res != -1 { return res }
        }
        return -1
    }

    private func check(_ target: Int) -> Int {
        var diff = Array(repeating: [Int](repeating: 0, count: n + 2), count: m + 2)
        var totalOps = 0
        for i in 1...m {
            for j in 1...n {
                diff[i][j] += diff[i - 1][j] + diff[i][j - 1] - diff[i - 1][j - 1]
                let curVal = grid[i - 1][j - 1] + diff[i][j]
                if curVal > target { return -1 }
                if curVal < target {
                    if i + k - 1 > m || j + k - 1 > n { return -1 }
                    let needed = target - curVal
                    totalOps += needed
                    diff[i][j] += needed
                    diff[i + k][j] -= needed
                    diff[i][j + k] -= needed
                    diff[i + k][j + k] += needed
                }
            }
        }
        return totalOps
    }
}
