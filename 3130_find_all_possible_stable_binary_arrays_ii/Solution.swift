// LeetCode 3130 - Find All Possible Stable Binary Arrays II
// https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/

class Solution {
    private let MOD = 1_000_000_007
    private var limit = 0
    private var f: [[[Int]]] = []

    func numberOfStableArrays(_ zero: Int, _ one: Int, _ limit: Int) -> Int {
        self.limit = limit
        f = Array(repeating: Array(repeating: [-1, -1], count: one + 1), count: zero + 1)
        return (dfs(zero, one, 0) + dfs(zero, one, 1)) % MOD
    }

    private func dfs(_ i: Int, _ j: Int, _ k: Int) -> Int {
        if i < 0 || j < 0 { return 0 }
        if i == 0 { return (k == 1 && j <= limit) ? 1 : 0 }
        if j == 0 { return (k == 0 && i <= limit) ? 1 : 0 }
        if f[i][j][k] != -1 { return f[i][j][k] }
        let res: Int
        if k == 0 {
            res = (dfs(i - 1, j, 0) + dfs(i - 1, j, 1) - dfs(i - limit - 1, j, 1) + MOD) % MOD
        } else {
            res = (dfs(i, j - 1, 0) + dfs(i, j - 1, 1) - dfs(i, j - limit - 1, 0) + MOD) % MOD
        }
        f[i][j][k] = res
        return res
    }
}
