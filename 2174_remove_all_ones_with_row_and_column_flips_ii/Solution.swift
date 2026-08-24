// LeetCode 2174 - Remove All Ones With Row and Column Flips II
// https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips-ii/

class Solution {
    func removeOnes(_ grid: [[Int]]) -> Int {
        var grid = grid
        let m = grid.count, n = grid[0].count
        var ones = [(Int, Int)]()
        for i in 0..<m {
            for j in 0..<n where grid[i][j] == 1 { ones.append((i, j)) }
        }
        if ones.isEmpty { return 0 }
        var ans = m + n
        func dfs(_ idx: Int, _ flips: Int) {
            if flips >= ans { return }
            var idx = idx
            while idx < ones.count && grid[ones[idx].0][ones[idx].1] == 0 { idx += 1 }
            if idx == ones.count { ans = flips; return }
            let (r, c) = ones[idx]
            var changed = [(Int, Int)]()
            for j in 0..<n where grid[r][j] == 1 { grid[r][j] = 0; changed.append((r, j)) }
            dfs(idx + 1, flips + 1)
            for p in changed { grid[p.0][p.1] = 1 }
            changed.removeAll()
            for i in 0..<m where grid[i][c] == 1 { grid[i][c] = 0; changed.append((i, c)) }
            dfs(idx + 1, flips + 1)
            for p in changed { grid[p.0][p.1] = 1 }
        }
        dfs(0, 0)
        return ans
    }
}
