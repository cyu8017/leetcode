// LeetCode 2083 - Substrings That Begin and End With the Same Letter
// https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter/

class Solution {
    func numberOfSubstrings(_ s: String) -> Int {
        var freq = [Int](repeating: 0, count: 26)
        var ans = 0
        for c in s {
            let i = Int(c.asciiValue! - 97)
            freq[i] += 1
            ans += freq[i]
        }
        return ans
    }
}
