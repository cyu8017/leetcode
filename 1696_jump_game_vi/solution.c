// LeetCode 1696 - Jump Game VI
// https://leetcode.com/problems/jump-game-vi/

#include <stdlib.h>

int maxResult(int* nums, int numsSize, int k) {
    int* qIdx = (int*)malloc((size_t)numsSize * sizeof(int));
    int* qVal = (int*)malloc((size_t)numsSize * sizeof(int));
    int head = 0, tail = 0;
    qIdx[tail] = 0; qVal[tail] = nums[0]; tail++;
    for (int i = 1; i < numsSize; i++) {
        while (head < tail && qIdx[head] < i - k) head++;
        int score = nums[i] + qVal[head];
        while (head < tail && qVal[tail - 1] <= score) tail--;
        qIdx[tail] = i; qVal[tail] = score; tail++;
    }
    int ans = qVal[tail - 1];
    free(qIdx); free(qVal);
    return ans;
}
