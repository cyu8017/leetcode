// LeetCode 3459 - Length of Longest V-Shaped Diagonal Segment
// https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

class Solution {
    func lenOfVDiagonal(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        let dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        let nextDir = [1, 2, 3, 0]
        var memo = [Int: Int]()
        func key(_ i: Int, _ j: Int, _ d: Int, _ turned: Int, _ expect: Int) -> Int {
            return ((((i * 101 + j) * 5 + d) * 3 + turned) * 5 + expect)
        }
        func dfs(_ i: Int, _ j: Int, _ d: Int, _ turned: Int, _ expect: Int) -> Int {
            if i < 0 || j < 0 || i >= m || j >= n || grid[i][j] != expect { return 0 }
            let k = key(i, j, d, turned, expect)
            if let c = memo[k] { return c }
            let ni = i + dirs[d].0, nj = j + dirs[d].1
            let nx = expect == 2 ? 0 : 2
            var best = 1 + dfs(ni, nj, d, turned, nx)
            if turned == 0 {
                let nd = nextDir[d]
                let ti = i + dirs[nd].0, tj = j + dirs[nd].1
                best = max(best, 1 + dfs(ti, tj, nd, 1, nx))
            }
            memo[k] = best
            return best
        }
        var ans = 0
        for i in 0..<m {
            for j in 0..<n where grid[i][j] == 1 {
                for d in 0..<4 {
                    let ni = i + dirs[d].0, nj = j + dirs[d].1
                    ans = max(ans, 1 + dfs(ni, nj, d, 0, 2))
                }
                if ans < 1 { ans = 1 }
            }
        }
        return ans
    }
}
