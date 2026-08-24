// LeetCode 3742 - Maximum Path Score In A Grid
// https://leetcode.com/problems/maximum-path-score-in-a-grid/

class Solution {
    private var grid = [[Int]]()
    private var f = [[[Int]]]()
    private var m = 0, n = 0
    private let INF = 1 << 30

    func maxPathScore(_ grid: [[Int]], _ k: Int) -> Int {
        self.grid = grid
        m = grid.count
        n = grid[0].count
        f = Array(repeating: Array(repeating: [Int](repeating: -1, count: k + 1), count: n), count: m)
        let ans = dfs(m - 1, n - 1, k)
        return ans < 0 ? -1 : ans
    }

    private func dfs(_ i: Int, _ j: Int, _ kk: Int) -> Int {
        if i < 0 || j < 0 || kk < 0 { return -INF }
        if i == 0 && j == 0 { return 0 }
        if f[i][j][kk] != -1 { return f[i][j][kk] }
        var res = grid[i][j]
        var nk = kk
        if grid[i][j] != 0 { nk -= 1 }
        let a = dfs(i - 1, j, nk)
        let b = dfs(i, j - 1, nk)
        res += max(a, b)
        f[i][j][kk] = res
        return res
    }
}
