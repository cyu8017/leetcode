// LeetCode 0583 - Delete Operation for Two Strings
// https://leetcode.com/problems/delete-operation-for-two-strings/

class Solution {
    func minDistance(_ word1: String, _ word2: String) -> Int {
        let a = Array(word1)
        let b = Array(word2)
        let m = a.count
        let n = b.count
        var prev = Array(repeating: 0, count: n + 1)
        var curr = Array(repeating: 0, count: n + 1)
        for i in 1...m {
            for j in 1...n {
                if a[i - 1] == b[j - 1] {
                    curr[j] = prev[j - 1] + 1
                } else {
                    curr[j] = max(prev[j], curr[j - 1])
                }
            }
            prev = curr
            curr = Array(repeating: 0, count: n + 1)
        }
        return m + n - 2 * prev[n]
    }
}
