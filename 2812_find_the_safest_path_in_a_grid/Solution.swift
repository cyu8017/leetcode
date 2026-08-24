// LeetCode 2812 - Find the Safest Path in a Grid
// https://leetcode.com/problems/find-the-safest-path-in-a-grid/

class Solution {
    func maximumSafenessFactor(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var dist = Array(repeating: Array(repeating: -1, count: n), count: n)
        var q: [(Int, Int)] = []
        for i in 0..<n {
            for j in 0..<n where grid[i][j] == 1 {
                dist[i][j] = 0
                q.append((i, j))
            }
        }
        let dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        var head = 0
        while head < q.count {
            let (x, y) = q[head]; head += 1
            for d in dirs {
                let ni = x + d.0, nj = y + d.1
                if ni >= 0 && ni < n && nj >= 0 && nj < n && dist[ni][nj] == -1 {
                    dist[ni][nj] = dist[x][y] + 1
                    q.append((ni, nj))
                }
            }
        }
        var lo = 0, hi = n * n, ans = 0
        while lo <= hi {
            let mid = (lo + hi) / 2
            if ok(dist, dirs, mid) {
                ans = mid
                lo = mid + 1
            } else {
                hi = mid - 1
            }
        }
        return ans
    }

    private func ok(_ dist: [[Int]], _ dirs: [(Int, Int)], _ sf: Int) -> Bool {
        let n = dist.count
        if dist[0][0] < sf { return false }
        var seen = Array(repeating: Array(repeating: false, count: n), count: n)
        var st = [(0, 0)]
        seen[0][0] = true
        while !st.isEmpty {
            let (x, y) = st.removeLast()
            if x == n - 1 && y == n - 1 { return true }
            for d in dirs {
                let ni = x + d.0, nj = y + d.1
                if ni >= 0 && ni < n && nj >= 0 && nj < n && !seen[ni][nj] && dist[ni][nj] >= sf {
                    seen[ni][nj] = true
                    st.append((ni, nj))
                }
            }
        }
        return false
    }
}
