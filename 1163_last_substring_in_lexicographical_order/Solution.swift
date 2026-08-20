// LeetCode 1163 - Last Substring in Lexicographical Order
// https://leetcode.com/problems/last-substring-in-lexicographical-order/

class Solution {
    func lastSubstring(_ s: String) -> String {
        let chars = Array(s)
        let n = chars.count
        var i = 0, j = 1, k = 0
        while j + k < n {
            if chars[i + k] == chars[j + k] {
                k += 1
            } else if chars[i + k] < chars[j + k] {
                i = max(i + k + 1, j)
                j = i + 1
                k = 0
            } else {
                j = j + k + 1
                k = 0
            }
        }
        return String(chars[i...])
    }
}
