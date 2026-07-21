// LeetCode 1881 - Maximum Value after Insertion
// https://leetcode.com/problems/maximum-value-after-insertion/

class Solution {
    func maxValue(_ n: String, _ x: Int) -> String {
        let chars = Array(n)
        let neg = chars[0] == "-"
        let start = neg ? 1 : 0
        let xStr = String(x)

        for i in start..<chars.count {
            let d = Int(String(chars[i]))!
            if neg {
                if d > x {
                    return String(chars[0..<i]) + xStr + String(chars[i...])
                }
            } else if d < x {
                return String(chars[0..<i]) + xStr + String(chars[i...])
            }
        }
        return n + xStr
    }
}
