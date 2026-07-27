// LeetCode 1694 - Reformat Phone Number
// https://leetcode.com/problems/reformat-phone-number/

class Solution {
    func reformatNumber(_ number: String) -> String {
        var s = String(number.filter { $0 >= "0" && $0 <= "9" })
        var out = [String]()
        while s.count > 4 {
            out.append(String(s.prefix(3)))
            s = String(s.dropFirst(3))
        }
        if s.count == 4 {
            out.append(String(s.prefix(2)))
            out.append(String(s.suffix(2)))
        } else if !s.isEmpty {
            out.append(s)
        }
        return out.joined(separator: "-")
    }
}
