// LeetCode 1915 - Number of Wonderful Substrings
// https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution {
    func wonderfulSubstrings(_ word: String) -> Int {
        var count = Array(repeating: 0, count: 1024)
        count[0] = 1
        var mask = 0, ans = 0
        for ch in word.utf8 {
            mask ^= 1 << Int(ch - 97)
            ans += count[mask]
            for bit in 0..<10 {
                ans += count[mask ^ (1 << bit)]
            }
            count[mask] += 1
        }
        return ans
    }
}
