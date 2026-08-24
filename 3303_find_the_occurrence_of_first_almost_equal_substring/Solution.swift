// LeetCode 3303 - Find the Occurrence of First Almost Equal Substring
// https://leetcode.com/problems/find-the-occurrence-of-first-almost-equal-substring/

class Solution {
    func minStartingIndex(_ s: String, _ pattern: String) -> Int {
        let s = Array(s), p = Array(pattern)
        let n = s.count, m = p.count
        if n < m { return -1 }
        for i in 0...(n - m) {
            var diff = 0
            for j in 0..<m {
                if s[i + j] != p[j] {
                    diff += 1
                    if diff > 1 { break }
                }
            }
            if diff <= 1 { return i }
        }
        return -1
    }
}
