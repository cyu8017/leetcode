// LeetCode 2852 - Sum of Remoteness of All Cells
// https://leetcode.com/problems/sum-of-remoteness-of-all-cells/

class Solution {
    func sumRemoteness(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        var seen = Array(repeating: Array(repeating: false, count: n), count: m)
        let dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        var total = 0
        for i in 0..<m {
            for j in 0..<n where grid[i][j] != -1 {
                total += grid[i][j]
            }
        }
        var ans = 0
        for i in 0..<m {
            for j in 0..<n {
                if grid[i][j] == -1 || seen[i][j] { continue }
                var q = [(i, j)]
                seen[i][j] = true
                var sum = 0, cnt = 0
                var head = 0
                while head < q.count {
                    let (x, y) = q[head]
                    head += 1
                    sum += grid[x][y]
                    cnt += 1
                    for d in dirs {
                        let ni = x + d[0], nj = y + d[1]
                        if ni >= 0 && nj >= 0 && ni < m && nj < n && !seen[ni][nj] && grid[ni][nj] != -1 {
                            seen[ni][nj] = true
                            q.append((ni, nj))
                        }
                    }
                }
                ans += (total - sum) * cnt
            }
        }
        return ans
    }
}
