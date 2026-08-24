// LeetCode 2664 - The Knight's Tour
// https://leetcode.com/problems/the-knights-tour/

class Solution {
    private let dirs = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]

    func tourOfKnight(_ m: Int, _ n: Int, _ r: Int, _ c: Int) -> [[Int]] {
        var ans = Array(repeating: Array(repeating: -1, count: n), count: m)
        _ = dfs(&ans, m, n, r, c, 0)
        return ans
    }

    private func dfs(_ ans: inout [[Int]], _ m: Int, _ n: Int, _ x: Int, _ y: Int, _ step: Int) -> Bool {
        ans[x][y] = step
        if step == m * n - 1 { return true }
        for d in dirs {
            let nx = x + d[0], ny = y + d[1]
            if nx >= 0 && nx < m && ny >= 0 && ny < n && ans[nx][ny] == -1 {
                if dfs(&ans, m, n, nx, ny, step + 1) { return true }
            }
        }
        ans[x][y] = -1
        return false
    }
}
