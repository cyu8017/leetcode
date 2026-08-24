// LeetCode 2850 - Minimum Moves to Spread Stones Over Grid
// https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/

class Solution {
    private var extras: [[Int]] = []
    private var zeros: [[Int]] = []
    private var best = 0

    func minimumMoves(_ grid: [[Int]]) -> Int {
        extras = []
        zeros = []
        for i in 0..<3 {
            for j in 0..<3 {
                if grid[i][j] == 0 {
                    zeros.append([i, j])
                } else if grid[i][j] > 1 {
                    for _ in 0..<(grid[i][j] - 1) {
                        extras.append([i, j])
                    }
                }
            }
        }
        if zeros.isEmpty { return 0 }
        best = 1 << 30
        dfs(0, 0)
        return best
    }

    private func dfs(_ i: Int, _ cost: Int) {
        if cost >= best { return }
        if i == zeros.count {
            best = cost
            return
        }
        for j in 0..<extras.count {
            if extras[j][0] < 0 { continue }
            let e = extras[j]
            extras[j] = [-1, e[1]]
            let d = abs(e[0] - zeros[i][0]) + abs(e[1] - zeros[i][1])
            dfs(i + 1, cost + d)
            extras[j] = e
        }
    }
}
