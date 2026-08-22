// LeetCode 3660 - Jump Game IX
// https://leetcode.com/problems/jump-game-ix/

#include <stdlib.h>
static int imax(int a,int b){return a>b?a:b;}
static int imin(int a,int b){return a<b?a:b;}
int* maxValue(int* nums, int numsSize, int* returnSize) {
    int n = numsSize;
    int* ans = (int*)calloc((size_t)n, sizeof(int));
    int* preMax = (int*)malloc((size_t)n * sizeof(int));
    preMax[0] = nums[0];
    for (int i = 1; i < n; i++) preMax[i] = imax(preMax[i - 1], nums[i]);
    int sufMin = 1 << 30;
    for (int i = n - 1; i >= 0; i--) {
        if (preMax[i] > sufMin) ans[i] = ans[i + 1];
        else ans[i] = preMax[i];
        sufMin = imin(sufMin, nums[i]);
    }
    free(preMax);
    *returnSize = n;
    return ans;
}
