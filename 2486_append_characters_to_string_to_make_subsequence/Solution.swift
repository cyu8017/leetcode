// LeetCode 2486 - Append Characters to String to Make Subsequence
// https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/

class Solution {
    func appendCharacters(_ s: String, _ t: String) -> Int {
        let sc = Array(s), tc = Array(t)
        var j = 0
        for i in 0..<sc.count where j < tc.count {
            if sc[i] == tc[j] { j += 1 }
        }
        return tc.count - j
    }
}
