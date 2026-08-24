// LeetCode 3481 - Apply Substitutions
// https://leetcode.com/problems/apply-substitutions/

class Solution {
    func applySubstitutions(_ replacements: [[String]], _ text: String) -> String {
        var mp = [String: String]()
        for r in replacements { mp[r[0]] = r[1] }
        func resolve(_ s: String) -> String {
            let chars = Array(s)
            var out = ""
            var i = 0
            while i < chars.count {
                if chars[i] == "%" {
                    var j = i + 1
                    while j < chars.count && chars[j] != "%" { j += 1 }
                    let key = String(chars[(i + 1)..<j])
                    out += resolve(mp[key] ?? "")
                    i = j + 1
                } else {
                    out.append(chars[i])
                    i += 1
                }
            }
            return out
        }
        return resolve(text)
    }
}
