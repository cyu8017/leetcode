// LeetCode 3758 - Convert Number Words To Digits
// https://leetcode.com/problems/convert-number-words-to-digits/

class Solution {
    func convertNumber(_ s: String) -> String {
        let d = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        let chars = Array(s)
        let n = chars.count
        var ans = ""
        var i = 0
        while i < n {
            var matched = false
            for j in 0..<10 {
                let m = d[j].count
                if i + m <= n && String(chars[i..<(i + m)]) == d[j] {
                    ans.append(Character(UnicodeScalar(48 + j)!))
                    i += m - 1
                    matched = true
                    break
                }
            }
            i += 1
        }
        return ans
    }
}
