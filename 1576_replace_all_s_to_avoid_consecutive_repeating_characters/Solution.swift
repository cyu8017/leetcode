// LeetCode 1576 - Replace All ?'s to Avoid Consecutive Repeating Characters
// https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

class Solution {
    func modifyString(_ s: String) -> String {
        var chars = Array(s)
        for i in 0..<chars.count where chars[i] == "?" {
            for c: Character in ["a", "b", "c"] {
                let leftOk = i == 0 || chars[i - 1] != c
                let rightOk = i + 1 == chars.count || chars[i + 1] != c
                if leftOk && rightOk {
                    chars[i] = c
                    break
                }
            }
        }
        return String(chars)
    }
}
