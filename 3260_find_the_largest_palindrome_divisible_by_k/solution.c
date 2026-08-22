// LeetCode 3260 - Find the Largest Palindrome Divisible by K
// https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/

#include <stdlib.h>
#include <string.h>

static char* repeat8(int n) {
    char* b = (char*)malloc((size_t)n + 1);
    for (int i = 0; i < n; i++) b[i] = '8';
    b[n] = 0;
    return b;
}

static int mod7(const char* s, int n) {
    int r = 0;
    for (int i = 0; i < n; i++) r = (r * 10 + (s[i] - '0')) % 7;
    return r;
}

static char* largestPal7(int n) {
    int halfLen = (n + 1) / 2;
    char* half = (char*)malloc((size_t)halfLen + 1);
    for (int i = 0; i < halfLen; i++) half[i] = '9';
    half[halfLen] = 0;
    char* pal = (char*)malloc((size_t)n + 1);
    for (;;) {
        memcpy(pal, half, (size_t)halfLen);
        for (int i = 0; i < n / 2; i++) pal[n - 1 - i] = pal[i];
        pal[n] = 0;
        if (mod7(pal, n) == 0) { free(half); return pal; }
        int i = halfLen - 1;
        while (i >= 0 && half[i] == '0') { half[i] = '9'; i--; }
        if (i < 0) break;
        half[i]--;
    }
    free(half); free(pal);
    char* empty = (char*)malloc(1); empty[0] = 0; return empty;
}

char* largestPalindrome(int n, int k) {
    char* digits = (char*)malloc((size_t)n + 1);
    for (int i = 0; i < n; i++) digits[i] = '9';
    digits[n] = 0;
    int half = (n + 1) / 2;
    switch (k) {
    case 1: case 3: case 9: return digits;
    case 2:
        digits[0] = '8'; digits[n - 1] = '8'; return digits;
    case 4:
        if (n == 1) { free(digits); char* r = (char*)malloc(2); r[0] = '8'; r[1] = 0; return r; }
        digits[0] = digits[1] = '8';
        digits[n - 1] = digits[n - 2] = '8';
        return digits;
    case 5:
        digits[0] = digits[n - 1] = '5'; return digits;
    case 8:
        if (n <= 2) { free(digits); return repeat8(n); }
        digits[0] = digits[1] = digits[2] = '8';
        digits[n - 1] = digits[n - 2] = digits[n - 3] = '8';
        return digits;
    case 6:
        if (n == 1) { free(digits); char* r = (char*)malloc(2); r[0] = '6'; r[1] = 0; return r; }
        digits[0] = digits[n - 1] = '8';
        {
            int sum = 16 + 9 * (n - 2);
            int need = sum % 3;
            if (need != 0) {
                int pos = half - 1;
                digits[pos] = (char)('0' + (digits[pos] - '0') - need);
                if (n % 2 == 0 || pos != n - 1 - pos) digits[n - 1 - pos] = digits[pos];
            }
        }
        return digits;
    case 7:
        free(digits);
        return largestPal7(n);
    }
    return digits;
}
