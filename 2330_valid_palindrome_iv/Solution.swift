// LeetCode 2330 - Valid Palindrome IV
// https://leetcode.com/problems/valid-palindrome-iv/

class Solution {
    func makePalindrome(_ s: String) -> Bool {
        let arr = Array(s)
        var diff = 0
        var i = 0, j = arr.count - 1
        while i < j {
            if arr[i] != arr[j] {
                diff += 1
                if diff > 2 { return false }
            }
            i += 1
            j -= 1
        }
        return true
    }
}
