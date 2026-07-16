// LeetCode 0266 - Palindrome Permutation
// https://leetcode.com/problems/palindrome-permutation/

class Solution {
    func canPermutePalindrome(_ s: String) -> Bool {
        var counts = Array(repeating: 0, count: 26)
        for char in s {
            counts[Int(char.asciiValue! - 97)] += 1
        }
        var odd = 0
        for count in counts where count % 2 != 0 {
            odd += 1
        }
        return odd <= 1
    }
}
