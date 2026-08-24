// LeetCode 2133 - Check if Every Row and Column Contains All Numbers
// https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

class Solution {
    func checkValid(_ matrix: [[Int]]) -> Bool {
        let n = matrix.count
        for i in 0..<n {
            var row = [Bool](repeating: false, count: n + 1)
            var col = [Bool](repeating: false, count: n + 1)
            for j in 0..<n {
                if row[matrix[i][j]] || col[matrix[j][i]] { return false }
                row[matrix[i][j]] = true
                col[matrix[j][i]] = true
            }
        }
        return true
    }
}
