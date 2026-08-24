// LeetCode 2946 - Matrix Similarity After Cyclic Shifts
// https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/

class Solution {
    func areSimilar(_ mat: [[Int]], _ k: Int) -> Bool {
        let m = mat.count, n = mat[0].count
        for i in 0..<m {
            var shift: Int
            if i % 2 == 0 {
                shift = n - (k % n)
                if shift == n { shift = 0 }
            } else {
                shift = k % n
            }
            for j in 0..<n where mat[i][j] != mat[i][(j + shift) % n] {
                return false
            }
        }
        return true
    }
}
