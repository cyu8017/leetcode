// LeetCode 1745 - Palindrome Partitioning IV
// https://leetcode.com/problems/palindrome-partitioning-iv/

class Solution {
    func checkPartitioning(_ s: String) -> Bool {
        let chars = Array(s.utf8)
        let n = chars.count
        var pal = [[Bool]](repeating: [Bool](repeating: false, count: n), count: n)
        for i in stride(from: n - 1, through: 0, by: -1) {
            for j in i..<n {
                pal[i][j] = chars[i] == chars[j] && (j - i < 2 || pal[i + 1][j - 1])
            }
        }
        for i in 0..<max(n - 2, 0) {
            for j in (i + 1)..<(n - 1) {
                if pal[0][i] && pal[i + 1][j] && pal[j + 1][n - 1] {
                    return true
                }
            }
        }
        return false
    }
}
