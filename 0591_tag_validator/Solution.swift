// LeetCode 0591 - Tag Validator
// https://leetcode.com/problems/tag-validator/

class Solution {
    func isValid(_ code: String) -> Bool {
        let chars = Array(code)
        let n = chars.count
        var stack = [String]()
        var i = 0
        func startsWith(_ s: String, _ i: Int) -> Bool {
            let arr = Array(s)
            if i + arr.count > n { return false }
            return Array(chars[i..<(i + arr.count)]) == arr
        }
        func indexOf(_ s: String, _ from: Int) -> Int {
            let arr = Array(s)
            var j = from
            while j + arr.count <= n {
                if Array(chars[j..<(j + arr.count)]) == arr { return j }
                j += 1
            }
            return -1
        }
        while i < n {
            if startsWith("<![CDATA[", i) {
                if stack.isEmpty { return false }
                let j = indexOf("]]>", i + 9)
                if j < 0 { return false }
                i = j + 3
            } else if startsWith("</", i) {
                let j = indexOf(">", i + 2)
                if j < 0 { return false }
                let tag = String(chars[(i + 2)..<j])
                if stack.isEmpty || stack.last != tag { return false }
                stack.removeLast()
                i = j + 1
                if stack.isEmpty && i < n { return false }
            } else if chars[i] == "<" {
                let j = indexOf(">", i + 1)
                if j < 0 { return false }
                let tag = String(chars[(i + 1)..<j])
                if tag.isEmpty || tag.count > 9 { return false }
                for ch in tag {
                    if ch < "A" || ch > "Z" { return false }
                }
                stack.append(tag)
                i = j + 1
            } else {
                if stack.isEmpty { return false }
                i += 1
            }
        }
        return stack.isEmpty
    }
}
