// LeetCode 3221 - Maximum Array Hopping Score II
// https://leetcode.com/problems/maximum-array-hopping-score-ii/

#include <stdlib.h>

long long maxScore(int* nums, int numsSize) {
    int* stk = malloc(numsSize * sizeof(int));
    int top = 0;
    for (int i = 0; i < numsSize; i++) {
        while (top > 0 && nums[stk[top - 1]] <= nums[i]) top--;
        stk[top++] = i;
    }
    long long ans = 0;
    int i = 0;
    for (int t = 0; t < top; t++) {
        int j = stk[t];
        ans += (long long)(j - i) * nums[j];
        i = j;
    }
    free(stk);
    return ans;
}
