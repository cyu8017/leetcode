// LeetCode 0934 - Shortest Bridge
// https://leetcode.com/problems/shortest-bridge/

class Solution {
    func shortestBridge(_ grid: [[Int]]) -> Int {
        var grid = grid
        let n = grid.count
        let dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        func dfs(_ r: Int, _ c: Int) {
            if r < 0 || r >= n || c < 0 || c >= n || grid[r][c] != 1 { return }
            grid[r][c] = 2
            for d in dirs { dfs(r + d[0], c + d[1]) }
        }
        var found = false
        for i in 0..<n {
            if found { break }
            for j in 0..<n where grid[i][j] == 1 {
                dfs(i, j)
                found = true
                break
            }
        }
        var q = [(Int, Int, Int)]()
        for i in 0..<n {
            for j in 0..<n where grid[i][j] == 2 { q.append((i, j, 0)) }
        }
        var qi = 0
        while qi < q.count {
            let (r, c, dist) = q[qi]
            qi += 1
            for d in dirs {
                let nr = r + d[0], nc = c + d[1]
                if nr < 0 || nr >= n || nc < 0 || nc >= n { continue }
                if grid[nr][nc] == 1 { return dist }
                if grid[nr][nc] == 0 {
                    grid[nr][nc] = 2
                    q.append((nr, nc, dist + 1))
                }
            }
        }
        return -1
    }
}
