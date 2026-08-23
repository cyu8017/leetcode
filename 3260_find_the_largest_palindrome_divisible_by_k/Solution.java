// LeetCode 3260 - Find the Largest Palindrome Divisible by K
// https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/

import java.util.Arrays;

class Solution {
    public String largestPalindrome(int n, int k) {
        char[] digits = repeat('9', n);
        int half = (n + 1) / 2;
        switch (k) {
            case 1:
            case 3:
            case 9:
                return new String(digits);
            case 2:
                digits[0] = digits[n - 1] = '8';
                return new String(digits);
            case 4:
                if (n == 1) return "8";
                digits[0] = digits[1] = digits[n - 1] = digits[n - 2] = '8';
                return new String(digits);
            case 5:
                digits[0] = digits[n - 1] = '5';
                return new String(digits);
            case 8:
                if (n <= 2) return new String(repeat('8', n));
                digits[0] = digits[1] = digits[2] = '8';
                digits[n - 1] = digits[n - 2] = digits[n - 3] = '8';
                return new String(digits);
            case 6: {
                if (n == 1) return "6";
                digits[0] = digits[n - 1] = '8';
                int sum = 16 + 9 * (n - 2);
                int need = sum % 3;
                if (need != 0) {
                    int pos = half - 1;
                    digits[pos] = (char) ('0' + (digits[pos] - '0') - need);
                    if (n % 2 == 0 || pos != n - 1 - pos) digits[n - 1 - pos] = digits[pos];
                }
                return new String(digits);
            }
            case 7:
                return largestPal7(n);
            default:
                return new String(digits);
        }
    }

    private char[] repeat(char c, int n) {
        char[] a = new char[n];
        Arrays.fill(a, c);
        return a;
    }

    private int mod7(String s) {
        int r = 0;
        for (int i = 0; i < s.length(); i++) r = (r * 10 + (s.charAt(i) - '0')) % 7;
        return r;
    }

    private String largestPal7(int n) {
        int halfLen = (n + 1) / 2;
        char[] half = repeat('9', halfLen);
        for (;;) {
            char[] pal = new char[n];
            for (int i = 0; i < halfLen; i++) pal[i] = half[i];
            for (int i = 0; i < n / 2; i++) pal[n - 1 - i] = pal[i];
            if (mod7(new String(pal)) == 0) return new String(pal);
            int idx = halfLen - 1;
            while (idx >= 0 && half[idx] == '0') {
                half[idx] = '9';
                idx--;
            }
            if (idx < 0) break;
            half[idx]--;
        }
        return "";
    }
}
