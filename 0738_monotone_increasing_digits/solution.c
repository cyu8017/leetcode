// LeetCode 0738 - Monotone Increasing Digits
// https://leetcode.com/problems/monotone-increasing-digits/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int monotoneIncreasingDigits(int n) {
    char digits[16];
    sprintf(digits, "%d", n);
    int len = (int)strlen(digits);
    int mark = len;
    for (int i = len - 1; i > 0; i--) {
        if (digits[i] < digits[i - 1]) {
            digits[i - 1]--;
            mark = i;
        }
    }
    for (int i = mark; i < len; i++) {
        digits[i] = '9';
    }
    return atoi(digits);
}
