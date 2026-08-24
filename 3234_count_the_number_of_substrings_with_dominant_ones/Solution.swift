// LeetCode 3234 - Count the Number of Substrings With Dominant Ones
// https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/

class Solution {
    func numberOfSubstrings(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var nxt = Array(repeating: 0, count: n + 1)
        nxt[n] = n
        for i in stride(from: n - 1, through: 0, by: -1) {
            nxt[i] = nxt[i + 1]
            if chars[i] == "0" { nxt[i] = i }
        }
        var ans = 0
        for i in 0..<n {
            var cnt0 = chars[i] == "0" ? 1 : 0
            var j = i
            while j < n && cnt0 * cnt0 <= n {
                let cnt1 = nxt[j + 1] - i - cnt0
                if cnt1 >= cnt0 * cnt0 {
                    ans += min(nxt[j + 1] - j, cnt1 - cnt0 * cnt0 + 1)
                }
                j = nxt[j + 1]
                cnt0 += 1
            }
        }
        return ans
    }
}
