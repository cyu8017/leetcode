// LeetCode 3713 - Longest Balanced Substring I
// https://leetcode.com/problems/longest-balanced-substring-i/

class Solution {
    func longestBalanced(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var ans = 0
        for i in 0..<n {
            var cnt = Array(repeating: 0, count: 26)
            var mx = 0, v = 0
            for j in i..<n {
                let c = Int(chars[j].asciiValue! - 97)
                cnt[c] += 1
                if cnt[c] == 1 { v += 1 }
                mx = max(mx, cnt[c])
                if mx * v == j - i + 1 { ans = max(ans, j - i + 1) }
            }
        }
        return ans
    }
}
