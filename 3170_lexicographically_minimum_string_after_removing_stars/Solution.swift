// LeetCode 3170 - Lexicographically Minimum String After Removing Stars
// https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/

class Solution {
    func clearStars(_ s: String) -> String {
        let chars = Array(s)
        let n = chars.count
        var g = Array(repeating: [Int](), count: 26)
        var rem = Array(repeating: false, count: n)
        let a = Character("a").asciiValue!
        for i in 0..<n {
            if chars[i] == "*" {
                rem[i] = true
                for j in 0..<26 where !g[j].isEmpty {
                    rem[g[j].removeLast()] = true
                    break
                }
            } else {
                g[Int(chars[i].asciiValue! - a)].append(i)
            }
        }
        return String(chars.enumerated().compactMap { rem[$0.offset] ? nil : $0.element })
    }
}
