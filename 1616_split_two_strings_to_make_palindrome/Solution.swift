// LeetCode 1616 - Split Two Strings to Make Palindrome
// https://leetcode.com/problems/split-two-strings-to-make-palindrome/

class Solution {
    func checkPalindromeFormation(_ a: String, _ b: String) -> Bool {
        let A = Array(a), B = Array(b)
        return check(A, B) || check(B, A)
    }

    private func check(_ x: [Character], _ y: [Character]) -> Bool {
        var i = 0, j = x.count - 1
        while i < j && x[i] == y[j] {
            i += 1
            j -= 1
        }
        return isPalindrome(x, i, j) || isPalindrome(y, i, j)
    }

    private func isPalindrome(_ s: [Character], _ i: Int, _ j: Int) -> Bool {
        var i = i, j = j
        while i < j {
            if s[i] != s[j] { return false }
            i += 1
            j -= 1
        }
        return true
    }
}
