// LeetCode 2373 - Largest Local Values in a Matrix
// https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution {
    func largestLocal(_ grid: [[Int]]) -> [[Int]] {
        let n = grid.count
        var ans = [[Int]](repeating: [Int](repeating: 0, count: n - 2), count: n - 2)
        for i in 0..<(n - 2) {
            for j in 0..<(n - 2) {
                var mx = 0
                for r in i..<(i + 3) {
                    for c in j..<(j + 3) { mx = max(mx, grid[r][c]) }
                }
                ans[i][j] = mx
            }
        }
        return ans
    }
}
