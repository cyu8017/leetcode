// LeetCode 1861 - Rotating the Box
// https://leetcode.com/problems/rotating-the-box/

class Solution {
    func rotateTheBox(_ boxGrid: [[Character]]) -> [[Character]] {
        let m = boxGrid.count
        let n = boxGrid[0].count
        var rotated = Array(repeating: Array(repeating: Character("."), count: m), count: n)

        for i in 0..<n {
            for j in 0..<m {
                rotated[i][j] = boxGrid[m - 1 - j][i]
            }
        }

        for col in 0..<m {
            var row = n - 1
            for i in stride(from: n - 1, through: 0, by: -1) {
                if rotated[i][col] == "*" {
                    row = i - 1
                } else if rotated[i][col] == "#" {
                    rotated[i][col] = "."
                    rotated[row][col] = "#"
                    row -= 1
                }
            }
        }

        return rotated
    }
}
