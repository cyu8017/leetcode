// LeetCode 0482 - License Key Formatting
// https://leetcode.com/problems/license-key-formatting/

class Solution {
    func licenseKeyFormatting(_ s: String, _ k: Int) -> String {
        let chars = s.filter { $0 != "-" }.map { String($0).uppercased() }
        if chars.isEmpty {
            return ""
        }
        var firstLen = chars.count % k
        if firstLen == 0 {
            firstLen = k
        }
        var parts = [chars.prefix(firstLen).joined()]
        var index = firstLen
        while index < chars.count {
            let end = min(index + k, chars.count)
            parts.append(Array(chars[index..<end]).joined())
            index += k
        }
        return parts.joined(separator: "-")
    }
}
