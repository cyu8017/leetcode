// LeetCode 2245 - Maximum Trailing Zeros in a Cornered Path
// https://leetcode.com/problems/maximum-trailing-zeros-in-a-cornered-path/

class Solution {
    func maxTrailingZeros(_ grid: [[Int]]) -> Int {
        func fact(_ x: Int) -> (Int, Int) {
            var x = x, t = 0, f = 0
            while x % 2 == 0 { t += 1; x /= 2 }
            while x % 5 == 0 { f += 1; x /= 5 }
            return (t, f)
        }
        let m = grid.count, n = grid[0].count
        var left2 = [[Int]](repeating: [Int](repeating: 0, count: n), count: m)
        var left5 = left2, up2 = left2, up5 = left2
        for i in 0..<m {
            for j in 0..<n {
                let p = fact(grid[i][j])
                left2[i][j] = p.0
                up2[i][j] = p.0
                left5[i][j] = p.1
                up5[i][j] = p.1
                if j > 0 {
                    left2[i][j] += left2[i][j - 1]
                    left5[i][j] += left5[i][j - 1]
                }
                if i > 0 {
                    up2[i][j] += up2[i - 1][j]
                    up5[i][j] += up5[i - 1][j]
                }
            }
        }
        var ans = 0
        for i in 0..<m {
            for j in 0..<n {
                let cell = fact(grid[i][j])
                let L2 = left2[i][j], L5 = left5[i][j]
                let R2 = left2[i][n - 1] - left2[i][j] + cell.0
                let R5 = left5[i][n - 1] - left5[i][j] + cell.1
                let U2 = up2[i][j], U5 = up5[i][j]
                let D2 = up2[m - 1][j] - up2[i][j] + cell.0
                let D5 = up5[m - 1][j] - up5[i][j] + cell.1
                let cands = [
                    (L2 + U2 - cell.0, L5 + U5 - cell.1),
                    (L2 + D2 - cell.0, L5 + D5 - cell.1),
                    (R2 + U2 - cell.0, R5 + U5 - cell.1),
                    (R2 + D2 - cell.0, R5 + D5 - cell.1)
                ]
                for c in cands { ans = max(ans, min(c.0, c.1)) }
            }
        }
        return ans
    }
}
