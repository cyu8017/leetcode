// LeetCode 0807 - Max Increase to Keep City Skyline
// https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution {
    func maxIncreaseKeepingSkyline(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        var rowMax = Array(repeating: 0, count: m)
        var colMax = Array(repeating: 0, count: n)
        for r in 0..<m {
            for c in 0..<n {
                rowMax[r] = max(rowMax[r], grid[r][c])
                colMax[c] = max(colMax[c], grid[r][c])
            }
        }
        var ans = 0
        for r in 0..<m {
            for c in 0..<n {
                ans += min(rowMax[r], colMax[c]) - grid[r][c]
            }
        }
        return ans
    }
}
