// LeetCode 0761 - Special Binary String
// https://leetcode.com/problems/special-binary-string/

class Solution {
    func makeLargestSpecial(_ s: String) -> String {
        var parts = [String]()
        var balance = 0, start = 0
        let chars = Array(s)
        for i in 0..<chars.count {
            balance += chars[i] == "1" ? 1 : -1
            if balance == 0 {
                let inner = start + 1 < i ? String(chars[(start + 1)..<i]) : ""
                parts.append("1" + makeLargestSpecial(inner) + "0")
                start = i + 1
            }
        }
        return parts.sorted(by: >).joined()
    }
}
