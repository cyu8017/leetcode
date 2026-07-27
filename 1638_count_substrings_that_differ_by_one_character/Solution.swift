// LeetCode 1638 - Count Substrings That Differ by One Character
// https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

class Solution {
    func countSubstrings(_ s: String, _ t: String) -> Int {
        let S = Array(s), T = Array(t)
        var ans = 0
        for i in 0..<S.count {
            for j in 0..<T.count {
                var diff = 0
                var k = 0
                while k < min(S.count - i, T.count - j) {
                    if S[i + k] != T[j + k] { diff += 1 }
                    if diff == 1 { ans += 1 }
                    else if diff > 1 { break }
                    k += 1
                }
            }
        }
        return ans
    }
}
