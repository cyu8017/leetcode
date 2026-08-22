// LeetCode 3878 - Count Good Subarrays
// https://leetcode.com/problems/count-good-subarrays/

#include <stdlib.h>

long long countGoodSubarrays(int* nums, int numsSize) {
    int n = numsSize;
    int* l = (int*)malloc((size_t)n * sizeof(int));
    int* r = (int*)malloc((size_t)n * sizeof(int));
    int* stk = (int*)malloc((size_t)n * sizeof(int));
    int top = 0;
    for (int i = 0; i < n; i++) l[i] = -1;
    for (int i = 0; i < n; i++) {
        int x = nums[i];
        while (top > 0 && nums[stk[top - 1]] < x && (nums[stk[top - 1]] | x) == x) top--;
        if (top > 0) l[i] = stk[top - 1];
        stk[top++] = i;
    }
    for (int i = 0; i < n; i++) r[i] = n;
    top = 0;
    for (int i = n - 1; i >= 0; i--) {
        while (top > 0 && (nums[stk[top - 1]] | nums[i]) == nums[i]) top--;
        if (top > 0) r[i] = stk[top - 1];
        stk[top++] = i;
    }
    long long ans = 0;
    for (int i = 0; i < n; i++) ans += (long long)(i - l[i]) * (r[i] - i);
    free(l); free(r); free(stk);
    return ans;
}
