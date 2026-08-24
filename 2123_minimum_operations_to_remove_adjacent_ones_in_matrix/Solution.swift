// LeetCode 2123 - Minimum Operations to Remove Adjacent Ones in Matrix
// https://leetcode.com/problems/minimum-operations-to-remove-adjacent-ones-in-matrix/

class Solution {
    func minimumOperations(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        var id = [[Int]](repeating: [Int](repeating: -1, count: n), count: m)
        var cnt = 0
        for i in 0..<m {
            for j in 0..<n where grid[i][j] == 1 {
                id[i][j] = cnt; cnt += 1
            }
        }
        var g = [[Int]](repeating: [], count: cnt)
        let dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] != 1 || (i + j) % 2 != 0 { continue }
                let u = id[i][j]
                for (di, dj) in dirs {
                    let ni = i + di, nj = j + dj
                    if ni >= 0 && nj >= 0 && ni < m && nj < n && grid[ni][nj] == 1 {
                        g[u].append(id[ni][nj])
                    }
                }
            }
        }
        var match = [Int](repeating: -1, count: cnt)
        func dfs(_ u: Int, _ seen: inout [Bool]) -> Bool {
            for v in g[u] {
                if seen[v] { continue }
                seen[v] = true
                if match[v] == -1 || dfs(match[v], &seen) {
                    match[v] = u
                    return true
                }
            }
            return false
        }
        var ans = 0
        for i in 0..<m {
            for j in 0..<n where id[i][j] >= 0 && (i + j) % 2 == 0 {
                var seen = [Bool](repeating: false, count: cnt)
                if dfs(id[i][j], &seen) { ans += 1 }
            }
        }
        return ans
    }
}
