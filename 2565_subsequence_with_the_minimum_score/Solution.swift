// LeetCode 2565 - Subsequence With the Minimum Score
// https://leetcode.com/problems/subsequence-with-the-minimum-score/

class Solution {
    func minimumScore(_ s: String, _ t: String) -> Int {
        let sc = Array(s), tc = Array(t)
        let n = sc.count, m = tc.count
        var left = [Int](repeating: -1, count: m)
        var right = [Int](repeating: -1, count: m)
        var j = 0
        for i in 0..<n where j < m {
            if sc[i] == tc[j] {
                left[j] = i
                j += 1
            }
        }
        j = m - 1
        for i in stride(from: n - 1, through: 0, by: -1) where j >= 0 {
            if sc[i] == tc[j] {
                right[j] = i
                j -= 1
            }
        }
        if m > 0 && left[m - 1] != -1 { return 0 }
        var ans = m
        for i in 0..<m {
            if right[i] != -1 {
                ans = min(ans, i)
                break
            }
        }
        for i in stride(from: m - 1, through: 0, by: -1) {
            if left[i] != -1 {
                ans = min(ans, m - 1 - i)
                break
            }
        }
        j = 0
        for i in 0..<m {
            if left[i] == -1 { break }
            while j < m && (right[j] == -1 || right[j] <= left[i]) { j += 1 }
            if j < m { ans = min(ans, j - i - 1) }
        }
        return ans
    }
}
