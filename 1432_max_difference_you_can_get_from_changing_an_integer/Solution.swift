// LeetCode 1432 - Max Difference You Can Get From Changing an Integer
// https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

class Solution {
    func maxDiff(_ num: Int) -> Int {
        let s = String(num)
        var high = s
        for char in s where char != "9" {
            high = s.replacingOccurrences(of: String(char), with: "9")
            break
        }
        var low = s
        let chars = Array(s)
        if chars[0] != "1" {
            low = s.replacingOccurrences(of: String(chars[0]), with: "1")
        } else {
            for char in chars.dropFirst() where char != "0" && char != "1" {
                low = s.replacingOccurrences(of: String(char), with: "0")
                break
            }
        }
        return Int(high)! - Int(low)!
    }
}
