// LeetCode 0722 - Remove Comments
// https://leetcode.com/problems/remove-comments/

class Solution {
    func removeComments(_ source: [String]) -> [String] {
        var result = [String]()
        var buffer = ""
        var inBlock = false
        for line in source {
            let chars = Array(line)
            var i = 0
            while i < chars.count {
                if inBlock {
                    if i + 1 < chars.count && chars[i] == "*" && chars[i + 1] == "/" {
                        inBlock = false
                        i += 2
                    } else { i += 1 }
                } else if i + 1 < chars.count && chars[i] == "/" && chars[i + 1] == "*" {
                    inBlock = true
                    i += 2
                } else if i + 1 < chars.count && chars[i] == "/" && chars[i + 1] == "/" {
                    break
                } else {
                    buffer.append(chars[i])
                    i += 1
                }
            }
            if !inBlock && !buffer.isEmpty {
                result.append(buffer)
                buffer = ""
            }
        }
        return result
    }
}
