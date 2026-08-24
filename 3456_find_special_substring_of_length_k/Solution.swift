// LeetCode 3456 - Find Special Substring of Length K
// https://leetcode.com/problems/find-special-substring-of-length-k/

class Solution {
    func hasSpecialSubstring(_ s: String, _ k: Int) -> Bool {
        let chars = Array(s)
        let n = chars.count
        if n < k { return false }
        for i in 0...(n - k) {
            var ok = true
            for j in (i + 1)..<(i + k) where chars[j] != chars[i] { ok = false; break }
            if !ok { continue }
            if i > 0 && chars[i - 1] == chars[i] { continue }
            if i + k < n && chars[i + k] == chars[i] { continue }
            return true
        }
        return false
    }
}
