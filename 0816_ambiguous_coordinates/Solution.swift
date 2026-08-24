// LeetCode 0816 - Ambiguous Coordinates
// https://leetcode.com/problems/ambiguous-coordinates/

class Solution {
    func ambiguousCoordinates(_ s: String) -> [String] {
        let chars = Array(s)
        let digits = String(chars[1..<(chars.count - 1)])
        var answer = [String]()
        for i in 1..<digits.count {
            let d = Array(digits)
            for left in candidates(String(d[0..<i])) {
                for right in candidates(String(d[i...])) {
                    answer.append("(" + left + ", " + right + ")")
                }
            }
        }
        return answer
    }

    private func candidates(_ frag: String) -> [String] {
        var options = [String]()
        if frag.isEmpty { return options }
        let chars = Array(frag)
        if chars.count > 1 && chars[0] == "0" && chars[chars.count - 1] == "0" { return options }
        if chars[0] == "0" && chars.count > 1 {
            if chars[chars.count - 1] != "0" { options.append("0." + String(chars[1...])) }
            return options
        }
        options.append(frag)
        if chars[chars.count - 1] == "0" { return options }
        for i in 1..<chars.count {
            options.append(String(chars[0..<i]) + "." + String(chars[i...]))
        }
        return options
    }
}
