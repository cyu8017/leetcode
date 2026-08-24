// LeetCode 2711 - Difference of Number of Distinct Values on Diagonals
// https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/

class Solution {
    func differenceOfDistinctValues(_ grid: [[Int]]) -> [[Int]] {
        let m = grid.count, n = grid[0].count
        var ans = Array(repeating: Array(repeating: 0, count: n), count: m)
        for i in 0..<m {
            for j in 0..<n {
                var top = Set<Int>()
                var bot = Set<Int>()
                var r = i - 1, c = j - 1
                while r >= 0 && c >= 0 {
                    top.insert(grid[r][c])
                    r -= 1; c -= 1
                }
                r = i + 1; c = j + 1
                while r < m && c < n {
                    bot.insert(grid[r][c])
                    r += 1; c += 1
                }
                ans[i][j] = abs(top.count - bot.count)
            }
        }
        return ans
    }
}
