// LeetCode 0400 - Nth Digit
// https://leetcode.com/problems/nth-digit/

#include <stdio.h>

int findNthDigit(int n) {
    int digits = 1;
    long long count = 9;
    long long start = 1;

    while (n > digits * count) {
        n -= (int)(digits * count);
        digits += 1;
        count *= 10;
        start *= 10;
    }

    long long number = start + (n - 1) / digits;
    char text[32];
    sprintf(text, "%lld", number);
    return text[(n - 1) % digits] - '0';
}
