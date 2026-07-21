// LeetCode 1886 - Determine Whether Matrix Can Be Obtained By Rotation
// https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution {
    func findRotation(_ mat: [[Int]], _ target: [[Int]]) -> Bool {
        var current = mat
        for _ in 0..<4 {
            if current == target {
                return true
            }
            current = rotate90(current)
        }
        return false
    }

    private func rotate90(_ matrix: [[Int]]) -> [[Int]] {
        let n = matrix.count
        var rotated = Array(repeating: Array(repeating: 0, count: n), count: n)
        for col in 0..<n {
            for row in 0..<n {
                rotated[col][row] = matrix[n - 1 - row][col]
            }
        }
        return rotated
    }
}
