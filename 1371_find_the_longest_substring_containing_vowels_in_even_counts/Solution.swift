// LeetCode 1371 - Find the Longest Substring Containing Vowels in Even Counts
// https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution {
    func findTheLongestSubstring(_ s: String) -> Int {
        let vowels = Array("aeiou")
        var first = [0: -1], mask = 0, ans = 0
        for (i, ch) in s.enumerated() {
            if let idx = vowels.firstIndex(of: ch) { mask ^= 1 << idx }
            if let f = first[mask] { ans = max(ans, i - f) }
            else { first[mask] = i }
        }
        return ans
    }
}
