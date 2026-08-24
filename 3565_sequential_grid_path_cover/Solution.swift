// LeetCode 3565 - Sequential Grid Path Cover
// https://leetcode.com/problems/sequential-grid-path-cover/

class Solution {
    var m = 0, n = 0
    var st: Int = 0
    var path = [[Int]]()
    let dirs = [-1, 0, 1, 0, -1]
    var grid = [[Int]]()

    func f(_ i: Int, _ j: Int) -> Int { i * n + j }

    func dfs(_ i: Int, _ j: Int, _ v0: Int) -> Bool {
        path.append([i, j])
        if path.count == m * n { return true }
        let idx = f(i, j)
        st |= 1 << idx
        var v = v0
        if grid[i][j] == v { v += 1 }
        for t in 0..<4 {
            let x = i + dirs[t], y = j + dirs[t + 1]
            if 0 <= x && x < m && 0 <= y && y < n {
                let idx2 = f(x, y)
                if ((st >> idx2) & 1) == 0 && (grid[x][y] == 0 || grid[x][y] == v) {
                    if dfs(x, y, v) { return true }
                }
            }
        }
        path.removeLast()
        st ^= 1 << idx
        return false
    }

    func findPath(_ grid: [[Int]], _ k: Int) -> [[Int]] {
        self.grid = grid
        m = grid.count
        n = grid[0].count
        st = 0
        path = []
        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] == 0 || grid[i][j] == 1 {
                    if dfs(i, j, 1) { return path }
                    path = []
                    st = 0
                }
            }
        }
        return []
    }
}
