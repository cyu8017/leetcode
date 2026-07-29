// LeetCode 1425 - Constrained Subsequence Sum
// https://leetcode.com/problems/constrained-subsequence-sum/

#include <stdlib.h>

int constrainedSubsetSum(int* nums, int numsSize, int k) {
    int* best = (int*)malloc(numsSize * sizeof(int));
    int* dq = (int*)malloc(numsSize * sizeof(int));
    int head = 0, tail = 0;
    int ans = nums[0];
    for (int i = 0; i < numsSize; i++) {
        while (head < tail && dq[head] < i - k) head++;
        best[i] = nums[i] + (head < tail && best[dq[head]] > 0 ? best[dq[head]] : 0);
        if (best[i] > ans) ans = best[i];
        while (head < tail && best[dq[tail - 1]] <= best[i]) tail--;
        dq[tail++] = i;
    }
    free(best); free(dq);
    return ans;
}
