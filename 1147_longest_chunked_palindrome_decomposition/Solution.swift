// LeetCode 1147 - Longest Chunked Palindrome Decomposition
// https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

class Solution {
    func longestDecomposition(_ text: String) -> Int {
        let chars = Array(text)
        let n = chars.count
        var ans = 0, i = 0
        while i < n - i {
            var found = false
            let limit = (n - 2 * i) / 2
            for length in 1...max(limit, 0) where length > 0 {
                if Array(chars[i..<(i + length)]) == Array(chars[(n - i - length)..<(n - i)]) {
                    ans += 2
                    i += length
                    found = true
                    break
                }
            }
            if !found { ans += 1; break }
        }
        return ans
    }
}
