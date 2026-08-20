// LeetCode 1946 - Largest Number After Mutating Substring
// https://leetcode.com/problems/largest-number-after-mutating-substring/

class Solution {
    func maximumNumber(_ num: String, _ change: [Int]) -> String {
        var chars = Array(num)
        var started = false
        for i in 0..<chars.count {
            let d = chars[i].wholeNumberValue!
            let mapped = change[d]
            if mapped > d {
                chars[i] = Character(String(mapped))
                started = true
            } else if mapped < d && started {
                break
            }
        }
        return String(chars)
    }
}
