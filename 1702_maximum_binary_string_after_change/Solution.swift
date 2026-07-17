// LeetCode 1702 - Maximum Binary String After Change
// https://leetcode.com/problems/maximum-binary-string-after-change/

class Solution {
    func maximumBinaryString(_ binary: String) -> String {
        let chars = Array(binary)
        var zeros = 0
        var first = -1
        for (i, ch) in chars.enumerated() {
            if ch == "0" {
                zeros += 1
                if first < 0 {
                    first = i
                }
            }
        }
        if zeros <= 1 {
            return binary
        }
        let n = chars.count
        return String(repeating: "1", count: first + zeros - 1) + "0"
            + String(repeating: "1", count: n - first - zeros)
    }
}
