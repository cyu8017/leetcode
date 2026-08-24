// LeetCode 0647 - Palindromic Substrings
// https://leetcode.com/problems/palindromic-substrings/

class Solution {
    func countSubstrings(_ s: String) -> Int {
        let chars = Array(s)
        var total = 0
        for i in 0..<chars.count {
            total += expand(chars, i, i)
            total += expand(chars, i, i + 1)
        }
        return total
    }

    private func expand(_ chars: [Character], _ left: Int, _ right: Int) -> Int {
        var left = left, right = right, count = 0
        while left >= 0 && right < chars.count && chars[left] == chars[right] {
            count += 1
            left -= 1
            right += 1
        }
        return count
    }
}
