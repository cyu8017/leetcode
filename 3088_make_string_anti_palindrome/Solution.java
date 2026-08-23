// LeetCode 3088 - Make String Anti-palindrome
// https://leetcode.com/problems/make-string-anti-palindrome/

import java.util.Arrays;

class Solution {
    public String makeAntiPalindrome(String s) {
        char[] arr = s.toCharArray();
        Arrays.sort(arr);
        int n = arr.length;
        int m = n / 2;
        if (arr[m] == arr[m - 1]) {
            int i = m;
            while (i < n && arr[i] == arr[i - 1]) i++;
            for (int j = m; j < n && arr[j] == arr[n - j - 1]; i++, j++) {
                if (i >= n) return "-1";
                char tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
            }
        }
        return new String(arr);
    }
}
