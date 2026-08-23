// LeetCode 3088 - Make String Anti-palindrome
// https://leetcode.com/problems/make-string-anti-palindrome/

using System;

public class Solution {
    public string MakeAntiPalindrome(string s) {
        char[] arr = s.ToCharArray();
        Array.Sort(arr);
        int n = arr.Length;
        int m = n / 2;
        if (arr[m] == arr[m - 1]) {
            int i = m;
            while (i < n && arr[i] == arr[i - 1]) i++;
            for (int j = m; j < n && arr[j] == arr[n - j - 1]; i++, j++) {
                if (i >= n) return "-1";
                char tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
            }
        }
        return new string(arr);
    }
}
