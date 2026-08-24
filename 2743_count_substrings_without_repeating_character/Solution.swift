// LeetCode 2743 - Count Substrings Without Repeating Character
// https://leetcode.com/problems/count-substrings-without-repeating-character/

class Solution {
    func numberOfSpecialSubstrings(_ s: String) -> Int {
        let chars = Array(s)
        var ans = 0, left = 0
        var cnt = Array(repeating: 0, count: 26)
        for i in chars.indices {
            let c = Int(chars[i].asciiValue! - 97)
            cnt[c] += 1
            while cnt[c] > 1 {
                cnt[Int(chars[left].asciiValue! - 97)] -= 1
                left += 1
            }
            ans += i - left + 1
        }
        return ans
    }
}
