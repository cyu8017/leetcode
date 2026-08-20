// LeetCode 1329 - Sort the Matrix Diagonally
// https://leetcode.com/problems/sort-the-matrix-diagonally/

class Solution {
    func diagonalSort(_ mat: [[Int]]) -> [[Int]] {
        var mat = mat
        var diagonals = [Int: [Int]]()
        for r in 0..<mat.count {
            for c in 0..<mat[r].count {
                diagonals[r - c, default: []].append(mat[r][c])
            }
        }
        for key in diagonals.keys { diagonals[key]!.sort(by: >) }
        for r in 0..<mat.count {
            for c in 0..<mat[r].count {
                mat[r][c] = diagonals[r - c]!.removeLast()
            }
        }
        return mat
    }
}
