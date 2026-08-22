// LeetCode 2197 - Replace Non-Coprime Numbers in Array
// https://leetcode.com/problems/replace-non-coprime-numbers-in-array/

#include <stdlib.h>

static int gcd2197(int a, int b) {
    while (b) { int t = a % b; a = b; b = t; }
    return a;
}

int* replaceNonCoprimes(int* nums, int numsSize, int* returnSize) {
    int* stack = (int*)malloc((size_t)numsSize * sizeof(int));
    int sn = 0;
    for (int i = 0; i < numsSize; i++) {
        long long x = nums[i];
        while (sn > 0) {
            int g = gcd2197(stack[sn - 1], (int)x);
            if (g == 1) break;
            x = (long long)stack[sn - 1] / g * x;
            sn--;
        }
        stack[sn++] = (int)x;
    }
    *returnSize = sn;
    return stack;
}
