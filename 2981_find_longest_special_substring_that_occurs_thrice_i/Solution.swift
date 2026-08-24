// LeetCode 2981 - Find Longest Special Substring That Occurs Thrice I
// https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i/

class Solution {
    func maximumLength(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var ans = -1
        for i in 0..<n {
            for j in i..<n {
                if chars[j] != chars[i] { break }
                let len = j - i + 1
                var cnt = 0
                var k = 0
                while k + len <= n {
                    var ok = true
                    for t in 0..<len where chars[k + t] != chars[i + t] {
                        ok = false
                        break
                    }
                    if ok { cnt += 1 }
                    k += 1
                }
                if cnt >= 3 { ans = max(ans, len) }
            }
        }
        return ans
    }
}
