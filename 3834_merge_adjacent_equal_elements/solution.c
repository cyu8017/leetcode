// LeetCode 3834 - Merge Adjacent Equal Elements
// https://leetcode.com/problems/merge-adjacent-equal-elements/

#include <stdlib.h>

long long* mergeAdjacent(int* nums, int numsSize, int* returnSize) {
    long long* stk = (long long*)malloc((size_t)numsSize * sizeof(long long));
    int top = 0;
    for (int i = 0; i < numsSize; i++) {
        stk[top++] = nums[i];
        while (top > 1 && stk[top - 1] == stk[top - 2]) {
            long long a = stk[--top];
            long long b = stk[--top];
            stk[top++] = a + b;
        }
    }
    *returnSize = top;
    return stk;
}
