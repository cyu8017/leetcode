// LeetCode 2578 - Split With Minimum Sum
// https://leetcode.com/problems/split-with-minimum-sum/

#include <stdlib.h>

static int cmpInt(const void* a, const void* b) {
    return *(const int*)a - *(const int*)b;
}

int splitNum(int num) {
    int digits[16], len = 0;
    while (num > 0) { digits[len++] = num % 10; num /= 10; }
    qsort(digits, (size_t)len, sizeof(int), cmpInt);
    int a = 0, b = 0;
    for (int i = 0; i < len; i++) {
        if (i % 2 == 0) a = a * 10 + digits[i];
        else b = b * 10 + digits[i];
    }
    return a + b;
}
