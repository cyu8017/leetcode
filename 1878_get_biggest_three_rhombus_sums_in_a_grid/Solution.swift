// LeetCode 1878 - Get Biggest Three Rhombus Sums in a Grid
// https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

class Solution {
    func getBiggestThree(_ grid: [[Int]]) -> [Int] {
        let m = grid.count
        let n = grid[0].count
        var s1 = Array(repeating: Array(repeating: 0, count: n + 2), count: m + 1)
        var s2 = Array(repeating: Array(repeating: 0, count: n + 2), count: m + 1)

        for i in 0..<m {
            for j in 0..<n {
                let value = grid[i][j]
                s1[i + 1][j + 1] = s1[i][j] + value
                s2[i + 1][j + 1] = s2[i][j + 2] + value
            }
        }

        var rhombusSums = Set<Int>()
        for i in 0..<m {
            for j in 0..<n {
                let value = grid[i][j]
                let row = i + 1
                let col = j + 1
                let limit = min(row - 1, m - row, col - 1, n - col)
                rhombusSums.insert(value)
                for k in 1...limit {
                    let a = s1[row + k][col] - s1[row][col - k]
                    let b = s1[row][col + k] - s1[row - k][col]
                    let c = s2[row][col - k] - s2[row - k][col]
                    let d = s2[row + k][col] - s2[row][col + k]
                    rhombusSums.insert(
                        a + b + c + d - grid[row + k - 1][col - 1] + grid[row - k - 1][col - 1]
                    )
                }
            }
        }

        return Array(rhombusSums.sorted(by: >).prefix(3))
    }
}
