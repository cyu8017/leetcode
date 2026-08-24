// LeetCode 0726 - Number of Atoms
// https://leetcode.com/problems/number-of-atoms/

class Solution {
    func countOfAtoms(_ formula: String) -> String {
        let chars = Array(formula)
        var st = [[String: Int]()]
        var i = 0
        let n = chars.count
        while i < n {
            if chars[i] == "(" {
                st.append([:])
                i += 1
            } else if chars[i] == ")" {
                i += 1
                let start = i
                while i < n && chars[i] >= "0" && chars[i] <= "9" { i += 1 }
                let mult = start < i ? Int(String(chars[start..<i]))! : 1
                let top = st.removeLast()
                for (k, v) in top {
                    st[st.count - 1][k, default: 0] += v * mult
                }
            } else {
                var j = i + 1
                while j < n && chars[j] >= "a" && chars[j] <= "z" { j += 1 }
                let atom = String(chars[i..<j])
                i = j
                let start = i
                while i < n && chars[i] >= "0" && chars[i] <= "9" { i += 1 }
                let count = start < i ? Int(String(chars[start..<i]))! : 1
                st[st.count - 1][atom, default: 0] += count
            }
        }
        return st.last!.keys.sorted().map { key in
            let c = st.last![key]!
            return c > 1 ? "\(key)\(c)" : key
        }.joined()
    }
}
