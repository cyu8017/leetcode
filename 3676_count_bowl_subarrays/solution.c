// LeetCode 3676 - Count Bowl Subarrays
// https://leetcode.com/problems/count-bowl-subarrays/

#include <stdlib.h>

long long bowlSubarrays(int* nums, int numsSize) {
    int n = numsSize;
    long long ans = 0;
    int* ngr = (int*)malloc((size_t)n * sizeof(int));
    int* ngl = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) { ngr[i] = -1; ngl[i] = -1; }
    int* stack = (int*)malloc((size_t)n * sizeof(int));
    int top = 0;
    for (int i = n - 1; i >= 0; i--) {
        while (top > 0 && nums[stack[top - 1]] < nums[i]) top--;
        if (top > 0) ngr[i] = stack[top - 1];
        stack[top++] = i;
    }
    top = 0;
    for (int i = 0; i < n; i++) {
        while (top > 0 && nums[stack[top - 1]] < nums[i]) top--;
        if (top > 0) ngl[i] = stack[top - 1];
        stack[top++] = i;
    }
    for (int i = 0; i < n; i++) {
        if (ngr[i] != -1 && ngr[i] - i >= 2) ans++;
        if (ngl[i] != -1 && i - ngl[i] >= 2) ans++;
    }
    free(ngr); free(ngl); free(stack);
    return ans;
}
