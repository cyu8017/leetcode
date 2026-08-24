// LeetCode 0741 - Cherry Pickup
// https://leetcode.com/problems/cherry-pickup/

class Solution {
    func cherryPickup(_ grid: [[Int]]) -> Int {
        let n = grid.count
        var memo = Array(repeating: Array(repeating: Array(repeating: Int.min, count: n), count: n), count: n)
        func dp(_ r1: Int, _ c1: Int, _ c2: Int) -> Int {
            let r2 = r1 + c1 - c2
            if r1 >= n || c1 >= n || r2 >= n || c2 >= n || grid[r1][c1] == -1 || grid[r2][c2] == -1 {
                return -1_000_000_000
            }
            if r1 == n - 1 && c1 == n - 1 { return grid[r1][c1] }
            if memo[r1][c1][c2] != Int.min { return memo[r1][c1][c2] }
            var cherries = grid[r1][c1]
            if r1 != r2 || c1 != c2 { cherries += grid[r2][c2] }
            cherries += max(max(dp(r1 + 1, c1, c2), dp(r1, c1 + 1, c2)),
                            max(dp(r1 + 1, c1, c2 + 1), dp(r1, c1 + 1, c2 + 1)))
            memo[r1][c1][c2] = cherries
            return cherries
        }
        return max(0, dp(0, 0, 0))
    }
}
