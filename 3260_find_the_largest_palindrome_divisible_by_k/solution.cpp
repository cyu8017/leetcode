// LeetCode 3260 - Find the Largest Palindrome Divisible by K
// https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/

#include <string>
#include <vector>

class Solution {
    std::string stringsRepeat8(int n) { return std::string(n, '8'); }

    int mod7(const std::string& s) {
        int r = 0;
        for (char c : s) r = (r * 10 + (c - '0')) % 7;
        return r;
    }

    std::string largestPal7(int n) {
        int halfLen = (n + 1) / 2;
        std::string half(halfLen, '9');
        for (;;) {
            std::string pal(n, '0');
            for (int i = 0; i < halfLen; i++) pal[i] = half[i];
            for (int i = 0; i < n / 2; i++) pal[n - 1 - i] = pal[i];
            if (mod7(pal) == 0) return pal;
            int i = halfLen - 1;
            while (i >= 0 && half[i] == '0') { half[i] = '9'; i--; }
            if (i < 0) break;
            half[i]--;
        }
        return "";
    }

public:
    std::string largestPalindrome(int n, int k) {
        std::string digits(n, '9');
        int half = (n + 1) / 2;
        switch (k) {
            case 1: case 3: case 9: return digits;
            case 2:
                digits[0] = digits[n - 1] = '8';
                return digits;
            case 4:
                if (n == 1) return "8";
                digits[0] = digits[1] = digits[n - 1] = digits[n - 2] = '8';
                return digits;
            case 5:
                digits[0] = digits[n - 1] = '5';
                return digits;
            case 8:
                if (n <= 2) return stringsRepeat8(n);
                digits[0] = digits[1] = digits[2] = '8';
                digits[n - 1] = digits[n - 2] = digits[n - 3] = '8';
                return digits;
            case 6: {
                if (n == 1) return "6";
                digits[0] = digits[n - 1] = '8';
                int sum = 16 + 9 * (n - 2);
                int need = sum % 3;
                if (need != 0) {
                    int pos = half - 1;
                    digits[pos] = char('0' + (digits[pos] - '0') - need);
                    if (n % 2 == 0 || pos != n - 1 - pos) digits[n - 1 - pos] = digits[pos];
                }
                return digits;
            }
            case 7: return largestPal7(n);
        }
        return digits;
    }
};
