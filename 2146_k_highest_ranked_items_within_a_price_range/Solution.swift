// LeetCode 2146 - K Highest Ranked Items Within a Price Range
// https://leetcode.com/problems/k-highest-ranked-items-within-a-price-range/

class Solution {
    func highestRankedKItems(_ grid: [[Int]], _ pricing: [Int], _ start: [Int], _ k: Int) -> [[Int]] {
        let m = grid.count, n = grid[0].count
        let low = pricing[0], high = pricing[1]
        var vis = [[Bool]](repeating: [Bool](repeating: false, count: n), count: m)
        var q = [(start[0], start[1], 0)]
        vis[start[0]][start[1]] = true
        var cands = [(Int, Int, Int, Int)]()
        var head = 0
        while head < q.count {
            let (r, c, d) = q[head]; head += 1
            if grid[r][c] >= low && grid[r][c] <= high { cands.append((d, grid[r][c], r, c)) }
            for (dr, dc) in [(1,0),(-1,0),(0,1),(0,-1)] {
                let nr = r + dr, nc = c + dc
                if nr >= 0 && nr < m && nc >= 0 && nc < n && !vis[nr][nc] && grid[nr][nc] != 0 {
                    vis[nr][nc] = true
                    q.append((nr, nc, d + 1))
                }
            }
        }
        cands.sort {
            if $0.0 != $1.0 { return $0.0 < $1.0 }
            if $0.1 != $1.1 { return $0.1 < $1.1 }
            if $0.2 != $1.2 { return $0.2 < $1.2 }
            return $0.3 < $1.3
        }
        return Array(cands.prefix(k).map { [$0.2, $0.3] })
    }
}
