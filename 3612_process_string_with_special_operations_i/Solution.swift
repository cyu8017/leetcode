// LeetCode 3612 - Process String with Special Operations I
// https://leetcode.com/problems/process-string-with-special-operations-i/

class Solution {
    func processStr(_ s: String) -> String {
        var result = [Character]()
        for c in s {
            if c.isLetter { result.append(c) }
            else if c == "*" {
                if !result.isEmpty { result.removeLast() }
            } else if c == "#" { result.append(contentsOf: result) }
            else if c == "%" { result.reverse() }
        }
        return String(result)
    }
}
