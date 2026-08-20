// LeetCode 1323 - Maximum 69 Number
// https://leetcode.com/problems/maximum-69-number/

class Solution {
    func maximum69Number (_ num: Int) -> Int {
        var chars = Array(String(num))
        if let i = chars.firstIndex(of: "6") { chars[i] = "9" }
        return Int(String(chars))!
    }
}
