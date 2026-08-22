// LeetCode 2160 - Minimum Sum of Four Digit Number After Splitting Digits
// https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

#include <stdlib.h>

static int cmpAsc(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

int minimumSum(int num) {
    int d[4] = {num / 1000, (num / 100) % 10, (num / 10) % 10, num % 10};
    qsort(d, 4, sizeof(int), cmpAsc);
    return 10 * d[0] + d[2] + 10 * d[1] + d[3];
}
