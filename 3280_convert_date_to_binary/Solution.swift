// LeetCode 3280 - Convert Date to Binary
// https://leetcode.com/problems/convert-date-to-binary/

class Solution {
    func convertDateToBinary(_ date: String) -> String {
        let parts = date.split(separator: "-").map { Int($0)! }
        return [toBinary(parts[0]), toBinary(parts[1]), toBinary(parts[2])].joined(separator: "-")
    }

    private func toBinary(_ v: Int) -> String {
        if v == 0 { return "0" }
        var x = v
        var s = ""
        while x > 0 {
            s = String(x & 1) + s
            x >>= 1
        }
        return s
    }
}
