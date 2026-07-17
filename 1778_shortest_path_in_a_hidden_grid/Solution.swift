// LeetCode 1778 - Shortest Path in a Hidden Grid
// https://leetcode.com/problems/shortest-path-in-a-hidden-grid/

class Solution {
    func findShortestPath(_ grid: [[Int]]) -> Int {
        let m = grid.count
        let n = grid[0].count
        var sr = 0
        var sc = 0
        for i in 0..<m {
            for j in 0..<n where grid[i][j] == -1 {
                sr = i
                sc = j
            }
        }
        let dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        var dist = [[Int]](repeating: [Int](repeating: -1, count: n), count: m)
        var queue = [(sr, sc)]
        var head = 0
        dist[sr][sc] = 0
        while head < queue.count {
            let (r, c) = queue[head]
            head += 1
            if grid[r][c] == 2 {
                return dist[r][c]
            }
            for (dr, dc) in dirs {
                let nr = r + dr
                let nc = c + dc
                if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] != 0
                    && dist[nr][nc] < 0 {
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
                }
            }
        }
        return -1
    }
}
