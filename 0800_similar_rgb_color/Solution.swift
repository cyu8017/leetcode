// LeetCode 0800 - Similar RGB Color
// https://leetcode.com/problems/similar-rgb-color/

class Solution {
    func similarRGB(_ color: String) -> String {
        let chars = Array(color)
        return "#" + closest(String(chars[1...2])) + closest(String(chars[3...4])) + closest(String(chars[5...6]))
    }

    private func closest(_ component: String) -> String {
        let value = Int(component, radix: 16)!
        let rounded = (value + 8) / 17
        return String(format: "%x%x", rounded, rounded)
    }
}
