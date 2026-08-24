// LeetCode 2482 - Difference Between Ones and Zeros in Row and Column
// https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/

class Solution {
    func onesMinusZeros(_ grid: [[Int]]) -> [[Int]] {
        let m = grid.count, n = grid[0].count
        var row = [Int](repeating: 0, count: m)
        var col = [Int](repeating: 0, count: n)
        for i in 0..<m {
            for j in 0..<n {
                row[i] += grid[i][j]
                col[j] += grid[i][j]
            }
        }
        var ans = [[Int]](repeating: [Int](repeating: 0, count: n), count: m)
        for i in 0..<m {
            for j in 0..<n {
                ans[i][j] = row[i] + col[j] - (m - row[i]) - (n - col[j])
            }
        }
        return ans
    }
}
