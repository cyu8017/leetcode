// LeetCode 1807 - Evaluate the Bracket Pairs of a String
// https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

class Solution {
    func evaluate(_ s: String, _ knowledge: [[String]]) -> String {
        var lookup = [String: String]()
        for pair in knowledge {
            lookup[pair[0]] = pair[1]
        }
        var result = ""
        let chars = Array(s)
        var i = 0
        while i < chars.count {
            if chars[i] == "(" {
                var j = i + 1
                while chars[j] != ")" { j += 1 }
                let key = String(chars[(i + 1)..<j])
                result += lookup[key] ?? "?"
                i = j + 1
            } else {
                result.append(chars[i])
                i += 1
            }
        }
        return result
    }
}
