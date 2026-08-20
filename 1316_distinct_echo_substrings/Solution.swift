// LeetCode 1316 - Distinct Echo Substrings
// https://leetcode.com/problems/distinct-echo-substrings/

class Solution {
    func distinctEchoSubstrings(_ text: String) -> Int {
        let s = Array(text), n = s.count
        var seen = Set<String>()
        guard n / 2 >= 1 else { return 0 }
        for length in 1...(n / 2) {
            var same = 0
            for i in 0..<(n - length) {
                if s[i] == s[i + length] { same += 1 } else { same = 0 }
                if same >= length {
                    seen.insert(String(s[(i - length + 1)..<(i + 1)]))
                }
            }
        }
        return seen.count
    }
}
