// LeetCode 2510 - Check if There is a Path With Equal Number of 0's And 1's
// https://leetcode.com/problems/check-if-there-is-a-path-with-equal-number-of-0s-and-1s/

class Solution {
    func isThereAPath(_ grid: [[Int]]) -> Bool {
        let m = grid.count, n = grid[0].count
        if (m + n - 1) % 2 != 0 { return false }
        let target = (m + n - 1) / 2
        var memo = [Int: Bool]()
        func dfs(_ r: Int, _ c: Int, _ bal: Int) -> Bool {
            if r >= m || c >= n { return false }
            let bal = bal + grid[r][c]
            if bal > target || bal + (m - 1 - r) + (n - 1 - c) < target { return false }
            if r == m - 1 && c == n - 1 { return bal == target }
            let k = (r << 20) | (c << 10) | bal
            if let cached = memo[k] { return cached }
            let ok = dfs(r + 1, c, bal) || dfs(r, c + 1, bal)
            memo[k] = ok
            return ok
        }
        return dfs(0, 0, 0)
    }
}
