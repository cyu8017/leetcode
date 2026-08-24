// LeetCode 2131 - Longest Palindrome by Concatenating Two Letter Words
// https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

class Solution {
    func longestPalindrome(_ words: [String]) -> Int {
        var freq = [String: Int]()
        for w in words { freq[w, default: 0] += 1 }
        var ans = 0
        var center = false
        for (w, c) in freq {
            let chars = Array(w)
            let rev = String([chars[1], chars[0]])
            if chars[0] == chars[1] {
                ans += (c / 2) * 4
                if c % 2 != 0 { center = true }
            } else if w < rev {
                ans += min(c, freq[rev, default: 0]) * 4
            }
        }
        if center { ans += 2 }
        return ans
    }
}
