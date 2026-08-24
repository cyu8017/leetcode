// LeetCode 2397 - Maximum Rows Covered by Columns
// https://leetcode.com/problems/maximum-rows-covered-by-columns/

class Solution {
    func maximumRows(_ matrix: [[Int]], _ numSelect: Int) -> Int {
        let m = matrix.count, n = matrix[0].count
        var ans = 0
        func dfs(_ col: Int, _ chosen: Int, _ mask: Int) {
            if chosen == numSelect {
                var covered = 0
                for i in 0..<m {
                    var ok = true
                    for j in 0..<n {
                        if matrix[i][j] == 1 && ((mask >> j) & 1) == 0 {
                            ok = false
                            break
                        }
                    }
                    if ok { covered += 1 }
                }
                ans = max(ans, covered)
                return
            }
            if col == n { return }
            dfs(col + 1, chosen + 1, mask | (1 << col))
            dfs(col + 1, chosen, mask)
        }
        dfs(0, 0, 0)
        return ans
    }
}
