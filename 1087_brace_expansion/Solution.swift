// LeetCode 1087 - Brace Expansion
// https://leetcode.com/problems/brace-expansion/

class Solution {
    func expand(_ s: String) -> [String] {
        let chars = Array(s)
        var groups: [[String]] = []
        var i = 0
        while i < chars.count {
            if chars[i] == "{" {
                var j = i + 1
                while chars[j] != "}" { j += 1 }
                let inner = String(chars[(i + 1)..<j])
                groups.append(inner.split(separator: ",").map(String.init).sorted())
                i = j + 1
            } else {
                groups.append([String(chars[i])])
                i += 1
            }
        }
        var ans = [""]
        for group in groups {
            var next: [String] = []
            for prefix in ans {
                for ch in group {
                    next.append(prefix + ch)
                }
            }
            ans = next
        }
        return ans
    }
}
