// LeetCode 3090 - Maximum Length Substring With Two Occurrences
// https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

class Solution {
    func maximumLengthSubstring(_ s: String) -> Int {
        let chars = Array(s)
        var l = 0, ans = 0
        var cnt = Array(repeating: 0, count: 26)
        let a = Character("a").asciiValue!
        for r in 0..<chars.count {
            let idx = Int(chars[r].asciiValue! - a)
            cnt[idx] += 1
            while cnt[idx] > 2 {
                cnt[Int(chars[l].asciiValue! - a)] -= 1
                l += 1
            }
            ans = max(ans, r - l + 1)
        }
        return ans
    }
}
