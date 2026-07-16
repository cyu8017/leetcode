// LeetCode 0249 - Group Shifted Strings
// https://leetcode.com/problems/group-shifted-strings/

class Solution {
    func groupStrings(_ strings: [String]) -> [[String]] {
        var groups: [String: [String]] = [:]
        var order: [String] = []

        for text in strings {
            let key: String
            if text.isEmpty {
                key = ""
            } else {
                let base = text.unicodeScalars.first!.value
                key = text.unicodeScalars
                    .map { String(($0.value - base + 26) % 26) }
                    .joined(separator: ",")
            }
            if groups[key] == nil {
                groups[key] = []
                order.append(key)
            }
            groups[key]!.append(text)
        }

        return order.map { groups[$0]! }
    }
}
