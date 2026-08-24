// LeetCode 3283 - Maximum Number of Moves to Kill All Pawns
// https://leetcode.com/problems/maximum-number-of-moves-to-kill-all-pawns/

class Solution {
    private let dirs = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]

    func maxMoves(_ kx: Int, _ ky: Int, _ positions: [[Int]]) -> Int {
        let n = positions.count
        var pts = Array(repeating: [0, 0], count: n + 1)
        pts[0] = [kx, ky]
        for i in 0..<n { pts[i + 1] = positions[i] }
        var dist = Array(repeating: [Int](), count: n + 1)
        for i in 0...n { dist[i] = knightDist(pts[i][0], pts[i][1], pts) }
        let N = 1 << n
        var memo = Array(repeating: Array(repeating: -1, count: n + 1), count: N)
        return dfs(0, 0, 0, n, N, dist, &memo)
    }

    private func knightDist(_ x: Int, _ y: Int, _ pts: [[Int]]) -> [Int] {
        let np = pts.count
        var ans = Array(repeating: -1, count: np)
        var vis = Array(repeating: Array(repeating: false, count: 50), count: 50)
        var q = [(x, y, 0)]
        vis[x][y] = true
        var need: [Int: [Int]] = [:]
        for i in 0..<np {
            let key = (pts[i][0] << 32) | (pts[i][1] & 0xffffffff)
            need[key, default: []].append(i)
        }
        var found = 0, qi = 0
        while qi < q.count && found < np {
            let (cx, cy, d) = q[qi]; qi += 1
            let key = (cx << 32) | (cy & 0xffffffff)
            if let idxs = need[key] {
                for i in idxs where ans[i] == -1 {
                    ans[i] = d
                    found += 1
                }
            }
            for dir in dirs {
                let nx = cx + dir[0], ny = cy + dir[1]
                if nx < 0 || ny < 0 || nx >= 50 || ny >= 50 || vis[nx][ny] { continue }
                vis[nx][ny] = true
                q.append((nx, ny, d + 1))
            }
        }
        return ans
    }

    private func dfs(_ mask: Int, _ cur: Int, _ turn: Int, _ n: Int, _ N: Int, _ dist: [[Int]], _ memo: inout [[Int]]) -> Int {
        if mask == N - 1 { return 0 }
        if memo[mask][cur] != -1 { return memo[mask][cur] }
        var best = turn == 0 ? -(1 << 30) : (1 << 30)
        for i in 0..<n where (mask & (1 << i)) == 0 {
            let d = dist[cur][i + 1]
            let v = d + dfs(mask | (1 << i), i + 1, 1 - turn, n, N, dist, &memo)
            if turn == 0 { best = max(best, v) }
            else { best = min(best, v) }
        }
        memo[mask][cur] = best
        return best
    }
}
