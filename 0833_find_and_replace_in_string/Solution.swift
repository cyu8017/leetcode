// LeetCode 0833 - Find And Replace in String
// https://leetcode.com/problems/find-and-replace-in-string/

class Solution {
    func findReplaceString(_ s: String, _ indices: [Int], _ sources: [String], _ targets: [String]) -> String {
        let chars = Array(s)
        var replaceLen = [Int: Int]()
        var replaceStr = [Int: String]()
        for k in 0..<indices.count {
            let i = indices[k]
            let src = Array(sources[k])
            if i + src.count <= chars.count && Array(chars[i..<(i + src.count)]) == src {
                replaceLen[i] = src.count
                replaceStr[i] = targets[k]
            }
        }
        var out = ""
        var i = 0
        while i < chars.count {
            if let t = replaceStr[i] {
                out += t
                i += replaceLen[i]!
            } else {
                out.append(chars[i])
                i += 1
            }
        }
        return out
    }
}
