// LeetCode 1926 - Nearest Exit from Entrance in Maze
// https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution {
    func nearestExit(_ maze: [[Character]], _ entrance: [Int]) -> Int {
        var maze = maze
        let m = maze.count, n = maze[0].count
        let er = entrance[0], ec = entrance[1]
        var q: [(Int, Int, Int)] = [(er, ec, 0)]
        var head = 0
        maze[er][ec] = "+"
        while head < q.count {
            let (r, c, d) = q[head]; head += 1
            for (nr, nc) in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)] {
                if nr >= 0 && nr < m && nc >= 0 && nc < n && maze[nr][nc] == "." {
                    if nr == 0 || nr == m - 1 || nc == 0 || nc == n - 1 { return d + 1 }
                    maze[nr][nc] = "+"
                    q.append((nr, nc, d + 1))
                }
            }
        }
        return -1
    }
}
