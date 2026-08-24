// LeetCode 2697 - Lexicographically Smallest Palindrome
// https://leetcode.com/problems/lexicographically-smallest-palindrome/

class Solution {
    func makeSmallestPalindrome(_ s: String) -> String {
        var arr = Array(s)
        let n = arr.count
        for i in 0..<(n / 2) {
            let c = min(arr[i], arr[n - 1 - i])
            arr[i] = c
            arr[n - 1 - i] = c
        }
        return String(arr)
    }
}
