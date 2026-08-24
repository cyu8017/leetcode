// LeetCode 3135 - Equalize Strings by Adding or Removing Characters at Ends
// https://leetcode.com/problems/equalize-strings-by-adding-or-removing-characters-at-ends/

class Solution {
    func minOperations(_ initial: String, _ target: String) -> Int {
        let a = Array(initial), b = Array(target)
        let m = a.count, n = b.count
        var f = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
        var mx = 0
        for i in 0..<m {
            for j in 0..<n where a[i] == b[j] {
                f[i + 1][j + 1] = f[i][j] + 1
                mx = max(mx, f[i + 1][j + 1])
            }
        }
        return m + n - 2 * mx
    }
}
