// LeetCode 3260 - Find the Largest Palindrome Divisible by K
// https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/

public class Solution {
    string StringsRepeat8(int n) => new string('8', n);

    int Mod7(string s) {
        int r = 0;
        foreach (char c in s) r = (r * 10 + (c - '0')) % 7;
        return r;
    }

    string LargestPal7(int n) {
        int halfLen = (n + 1) / 2;
        char[] half = new string('9', halfLen).ToCharArray();
        for (;;) {
            char[] pal = new char[n];
            for (int i = 0; i < n; i++) pal[i] = '0';
            for (int i = 0; i < halfLen; i++) pal[i] = half[i];
            for (int i = 0; i < n / 2; i++) pal[n - 1 - i] = pal[i];
            if (Mod7(new string(pal)) == 0) return new string(pal);
            int idx = halfLen - 1;
            while (idx >= 0 && half[idx] == '0') { half[idx] = '9'; idx--; }
            if (idx < 0) break;
            half[idx]--;
        }
        return "";
    }

    public string LargestPalindrome(int n, int k) {
        char[] digits = new string('9', n).ToCharArray();
        int half = (n + 1) / 2;
        switch (k) {
            case 1: case 3: case 9: return new string(digits);
            case 2:
                digits[0] = digits[n - 1] = '8';
                return new string(digits);
            case 4:
                if (n == 1) return "8";
                digits[0] = digits[1] = digits[n - 1] = digits[n - 2] = '8';
                return new string(digits);
            case 5:
                digits[0] = digits[n - 1] = '5';
                return new string(digits);
            case 8:
                if (n <= 2) return StringsRepeat8(n);
                digits[0] = digits[1] = digits[2] = '8';
                digits[n - 1] = digits[n - 2] = digits[n - 3] = '8';
                return new string(digits);
            case 6: {
                if (n == 1) return "6";
                digits[0] = digits[n - 1] = '8';
                int sum = 16 + 9 * (n - 2);
                int need = sum % 3;
                if (need != 0) {
                    int pos = half - 1;
                    digits[pos] = (char)('0' + (digits[pos] - '0') - need);
                    if (n % 2 == 0 || pos != n - 1 - pos) digits[n - 1 - pos] = digits[pos];
                }
                return new string(digits);
            }
            case 7: return LargestPal7(n);
        }
        return new string(digits);
    }
}
