// LeetCode 1556 - Thousand Separator
// https://leetcode.com/problems/thousand-separator/

class Solution {
    func thousandSeparator(_ n: Int) -> String {
        var s = String(n)
        var parts = [String]()
        while !s.isEmpty {
            let start = max(0, s.count - 3)
            parts.append(String(s[s.index(s.startIndex, offsetBy: start)...]))
            s = String(s.prefix(start))
        }
        return parts.reversed().joined(separator: ".")
    }
}
