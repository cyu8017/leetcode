// LeetCode 2814 - Minimum Time Takes to Reach Destination Without Drowning
// https://leetcode.com/problems/minimum-time-takes-to-reach-destination-without-drowning/

class Solution {
    func minimumSeconds(_ land: [[String]]) -> Int {
        let m = land.count, n = land[0].count
        let INF = 1 << 30
        var water = Array(repeating: Array(repeating: INF, count: n), count: m)
        var wq: [(Int, Int)] = []
        var sx = 0, sy = 0, dx = 0, dy = 0
        for i in 0..<m {
            for j in 0..<n {
                switch land[i][j] {
                case "*":
                    water[i][j] = 0
                    wq.append((i, j))
                case "S":
                    sx = i; sy = j
                case "D":
                    dx = i; dy = j
                default:
                    break
                }
            }
        }
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        var head = 0
        while head < wq.count {
            let (x, y) = wq[head]; head += 1
            for d in dirs {
                let ni = x + d.0, nj = y + d.1
                if ni < 0 || ni >= m || nj < 0 || nj >= n { continue }
                let cell = land[ni][nj]
                if cell == "X" || cell == "D" { continue }
                if water[ni][nj] > water[x][y] + 1 {
                    water[ni][nj] = water[x][y] + 1
                    wq.append((ni, nj))
                }
            }
        }
        var dist = Array(repeating: Array(repeating: -1, count: n), count: m)
        var q = [(sx, sy)]
        dist[sx][sy] = 0
        head = 0
        while head < q.count {
            let (x, y) = q[head]; head += 1
            if x == dx && y == dy { return dist[x][y] }
            for d in dirs {
                let ni = x + d.0, nj = y + d.1
                if ni < 0 || ni >= m || nj < 0 || nj >= n || dist[ni][nj] != -1 { continue }
                if land[ni][nj] == "X" { continue }
                let nd = dist[x][y] + 1
                if land[ni][nj] != "D" && nd >= water[ni][nj] { continue }
                dist[ni][nj] = nd
                q.append((ni, nj))
            }
        }
        return -1
    }
}
