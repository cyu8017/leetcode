// LeetCode 3619 - Count Islands With Total Value Divisible by K
// https://leetcode.com/problems/count-islands-with-total-value-divisible-by-k/

class Solution {
    var grid = [[Int]]()
    var m = 0, n = 0
    let dirs = [-1, 0, 1, 0, -1]

    func dfs(_ i: Int, _ j: Int) -> Int {
        var s = grid[i][j]
        grid[i][j] = 0
        for d in 0..<4 {
            let x = i + dirs[d], y = j + dirs[d + 1]
            if x >= 0 && x < m && y >= 0 && y < n && grid[x][y] > 0 { s += dfs(x, y) }
        }
        return s
    }

    func countIslands(_ grid: [[Int]], _ k: Int) -> Int {
        self.grid = grid
        m = grid.count
        n = grid[0].count
        var ans = 0
        for i in 0..<m {
            for j in 0..<n {
                if self.grid[i][j] > 0 && dfs(i, j) % k == 0 { ans += 1 }
            }
        }
        return ans
    }
}
