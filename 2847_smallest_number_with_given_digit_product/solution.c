// LeetCode 2847 - Smallest Number With Given Digit Product
// https://leetcode.com/problems/smallest-number-with-given-digit-product/

#include <stdlib.h>
#include <string.h>

char* smallestNumber(long long n) {
    if (n == 0) {
        char* r = (char*)malloc(2); strcpy(r, "0"); return r;
    }
    if (n == 1) {
        char* r = (char*)malloc(2); strcpy(r, "1"); return r;
    }
    char digits[64];
    int len = 0;
    for (int d = 9; d >= 2; d--) {
        while (n % d == 0) {
            digits[len++] = (char)('0' + d);
            n /= d;
        }
    }
    if (n > 1) {
        char* r = (char*)malloc(3); strcpy(r, "-1"); return r;
    }
    for (int i = 0, j = len - 1; i < j; i++, j--) {
        char t = digits[i]; digits[i] = digits[j]; digits[j] = t;
    }
    digits[len] = 0;
    char* r = (char*)malloc(len + 1);
    strcpy(r, digits);
    return r;
}
