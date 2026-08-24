// LeetCode 3088 - Make String Anti-palindrome
// https://leetcode.com/problems/make-string-anti-palindrome/

class Solution {
    func makeAntiPalindrome(_ s: String) -> String {
        var arr = Array(s).sorted()
        let n = arr.count
        let m = n / 2
        if arr[m] == arr[m - 1] {
            var i = m
            while i < n && arr[i] == arr[i - 1] { i += 1 }
            var j = m
            while j < n && arr[j] == arr[n - j - 1] {
                if i >= n { return "-1" }
                arr.swapAt(i, j)
                i += 1
                j += 1
            }
        }
        return String(arr)
    }
}
