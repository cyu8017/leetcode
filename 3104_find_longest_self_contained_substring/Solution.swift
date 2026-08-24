// LeetCode 3104 - Find Longest Self-Contained Substring
// https://leetcode.com/problems/find-longest-self-contained-substring/

class Solution {
    func maxSubstringLength(_ s: String) -> Int {
        var first = Array(repeating: -1, count: 26)
        var last = Array(repeating: 0, count: 26)
        let chars = Array(s)
        let a = Character("a").asciiValue!
        let n = chars.count
        for i in 0..<n {
            let j = Int(chars[i].asciiValue! - a)
            if first[j] == -1 { first[j] = i }
            last[j] = i
        }
        var ans = -1
        for k in 0..<26 {
            let i = first[k]
            if i == -1 { continue }
            var mx = last[k]
            for j in i..<n {
                let ch = Int(chars[j].asciiValue! - a)
                if first[ch] < i { break }
                mx = max(mx, last[ch])
                if mx == j && j - i + 1 < n { ans = max(ans, j - i + 1) }
            }
        }
        return ans
    }
}
