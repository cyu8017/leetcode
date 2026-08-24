// LeetCode 0750 - Number Of Corner Rectangles
// https://leetcode.com/problems/number-of-corner-rectangles/

class Solution {
    func countCornerRectangles(_ grid: [[Int]]) -> Int {
        let m = grid.count, n = grid[0].count
        var ans = 0
        for i in 0..<m {
            for j in (i + 1)..<m {
                var ones = 0
                for c in 0..<n where grid[i][c] == 1 && grid[j][c] == 1 { ones += 1 }
                ans += ones * (ones - 1) / 2
            }
        }
        return ans
    }
}
