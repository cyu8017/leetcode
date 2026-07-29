// LeetCode 1317 - Convert Integer to the Sum of Two No-Zero Integers
// https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

#include <stdlib.h>
#include <stdbool.h>

static bool valid(int v) {
    while (v) { if (v % 10 == 0) return false; v /= 10; }
    return true;
}

int* getNoZeroIntegers(int n, int* returnSize) {
    int* ans = (int*)malloc(2 * sizeof(int));
    for (int first = 1; first < n; first++) {
        if (valid(first) && valid(n - first)) {
            ans[0] = first; ans[1] = n - first;
            *returnSize = 2;
            return ans;
        }
    }
    *returnSize = 0;
    return ans;
}
