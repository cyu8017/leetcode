// LeetCode 2595 - Number of Even and Odd Bits
// https://leetcode.com/problems/number-of-even-and-odd-bits/

#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* evenOddBit(int n, int* returnSize) {
    int even = 0, odd = 0, i = 0;
    while (n > 0) {
        if (n & 1) {
            if (i % 2 == 0) even++;
            else odd++;
        }
        n >>= 1;
        i++;
    }
    int* ans = (int*)malloc(2 * sizeof(int));
    ans[0] = even; ans[1] = odd;
    *returnSize = 2;
    return ans;
}
