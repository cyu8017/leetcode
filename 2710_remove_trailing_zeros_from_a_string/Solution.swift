// LeetCode 2710 - Remove Trailing Zeros From a String
// https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

class Solution {
    func removeTrailingZeros(_ num: String) -> String {
        var end = num.count
        let chars = Array(num)
        while end > 0 && chars[end - 1] == "0" { end -= 1 }
        return String(chars[0..<end])
    }
}
