// LeetCode 2155 - All Divisions With the Highest Score of a Binary Array
// https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

#include <stdlib.h>

int* maxScoreIndices(int* nums, int numsSize, int* returnSize) {
    int n = numsSize, total1 = 0;
    for (int i = 0; i < n; i++) total1 += nums[i];
    int* ans = (int*)malloc((size_t)(n + 1) * sizeof(int));
    int an = 0, best = total1, left0 = 0, right1 = total1;
    ans[an++] = 0;
    for (int i = 0; i < n; i++) {
        if (nums[i] == 0) left0++;
        else right1--;
        int score = left0 + right1;
        if (score > best) { best = score; an = 0; ans[an++] = i + 1; }
        else if (score == best) ans[an++] = i + 1;
    }
    *returnSize = an;
    return ans;
}
