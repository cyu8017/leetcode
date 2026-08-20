// LeetCode 1271 - Hexspeak
// https://leetcode.com/problems/hexspeak/

class Solution {
    func toHexspeak(_ num: String) -> String {
        var n = Int(num)!
        var hex = ""
        if n == 0 { hex = "0" }
        while n > 0 {
            let d = n % 16
            if d == 10 { hex = "A" + hex }
            else if d == 11 { hex = "B" + hex }
            else if d == 12 { hex = "C" + hex }
            else if d == 13 { hex = "D" + hex }
            else if d == 14 { hex = "E" + hex }
            else if d == 15 { hex = "F" + hex }
            else { hex = String(d) + hex }
            n /= 16
        }
        var ans = ""
        for ch in hex {
            if ch == "0" { ans.append("O") }
            else if ch == "1" { ans.append("I") }
            else if "A"..."F" ~= ch { ans.append(ch) }
            else { return "ERROR" }
        }
        return ans
    }
}
