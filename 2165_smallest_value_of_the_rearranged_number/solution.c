// LeetCode 2165 - Smallest Value of the Rearranged Number
// https://leetcode.com/problems/smallest-value-of-the-rearranged-number/

#include <stdlib.h>

static int cmpAscC(const void* a, const void* b) { return *(const char*)a - *(const char*)b; }
static int cmpDescC(const void* a, const void* b) { return *(const char*)b - *(const char*)a; }

long long smallestNumber(long long num) {
    if (num == 0) return 0;
    int neg = num < 0;
    if (neg) num = -num;
    char digits[24];
    int n = 0;
    while (num > 0) { digits[n++] = (char)('0' + num % 10); num /= 10; }
    if (neg) {
        qsort(digits, (size_t)n, 1, cmpDescC);
        long long ans = 0;
        for (int i = 0; i < n; i++) ans = ans * 10 + (digits[i] - '0');
        return -ans;
    }
    qsort(digits, (size_t)n, 1, cmpAscC);
    if (digits[0] == '0') {
        for (int i = 1; i < n; i++) if (digits[i] != '0') {
            char t = digits[0]; digits[0] = digits[i]; digits[i] = t; break;
        }
    }
    long long ans = 0;
    for (int i = 0; i < n; i++) ans = ans * 10 + (digits[i] - '0');
    return ans;
}
