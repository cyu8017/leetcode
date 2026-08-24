// LeetCode 3844 - Longest Almost Palindromic Substring
// https://leetcode.com/problems/longest-almost-palindromic-substring/

class Solution {
    func almostPalindromic(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        var ans = 0
        for i in 0..<n {
            ans = max(ans, max(expand(chars, i, i), expand(chars, i, i + 1)))
        }
        return ans
    }

    private func expand(_ s: [Character], _ l: Int, _ r: Int) -> Int {
        let n = s.count
        var l = l, r = r
        while l >= 0 && r < n && s[l] == s[r] { l -= 1; r += 1 }
        var l1 = l - 1, r1 = r, l2 = l, r2 = r + 1
        while l1 >= 0 && r1 < n && s[l1] == s[r1] { l1 -= 1; r1 += 1 }
        while l2 >= 0 && r2 < n && s[l2] == s[r2] { l2 -= 1; r2 += 1 }
        return min(n, max(r1 - l1 - 1, r2 - l2 - 1))
    }
}
