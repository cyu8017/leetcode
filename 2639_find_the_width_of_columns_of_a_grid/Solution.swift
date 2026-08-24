// LeetCode 2639 - Find the Width of Columns of a Grid
// https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/

class Solution {
    func findColumnWidth(_ grid: [[Int]]) -> [Int] {
        let n = grid[0].count
        var ans = Array(repeating: 0, count: n)
        for row in grid {
            for j in 0..<n {
                ans[j] = max(ans[j], width(row[j]))
            }
        }
        return ans
    }

    private func width(_ x0: Int) -> Int {
        if x0 == 0 { return 1 }
        var x = x0
        var w = 0
        if x < 0 {
            w += 1
            x = -x
        }
        while x > 0 {
            w += 1
            x /= 10
        }
        return w
    }
}
