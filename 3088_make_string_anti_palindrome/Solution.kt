// LeetCode 3088 - Make String Anti-palindrome
// https://leetcode.com/problems/make-string-anti-palindrome/

class Solution {
    fun makeAntiPalindrome(s: String): String {
        var arr = s.toCharArray()
        arr.sort()
        var n = arr.size
        var m = n / 2
        if (arr[m] == arr[m - 1]) {
            var i = m
            while (i < n && arr[i] == arr[i - 1]) i++
            var j = m
            while (j < n && arr[j] == arr[n - j - 1]) {
                if (i >= n) return "-1"
                var tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp
                i++, j++
            }
        }
        return String(arr)
    }
}
