// LeetCode 3537 - Fill a Special Grid
// https://leetcode.com/problems/fill-a-special-grid/

class Solution {
    var ans = [[Int]]()
    var val = 0

    func specialGrid(_ n: Int) -> [[Int]] {
        let m = 1 << n
        ans = Array(repeating: Array(repeating: 0, count: m), count: m)
        val = 0
        dfs(0, m - 1, m)
        return ans
    }

    func dfs(_ x: Int, _ y: Int, _ k: Int) {
        if k == 1 {
            ans[x][y] = val
            val += 1
            return
        }
        let h = k / 2
        dfs(x, y, h)
        dfs(x + h, y, h)
        dfs(x + h, y - h, h)
        dfs(x, y - h, h)
    }
}
