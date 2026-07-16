// LeetCode 0486 - Predict the Winner
// https://leetcode.com/problems/predict-the-winner/

#include <stdbool.h>
#include <stdlib.h>

bool predictTheWinner(int* nums, int numsSize) {
    int** dp = (int**)malloc((size_t)numsSize * sizeof(int*));
    for (int index = 0; index < numsSize; index++) {
        dp[index] = (int*)calloc((size_t)numsSize, sizeof(int));
        dp[index][index] = nums[index];
    }
    for (int length = 2; length <= numsSize; length++) {
        for (int left = 0; left + length - 1 < numsSize; left++) {
            int right = left + length - 1;
            int leftScore = nums[left] - dp[left + 1][right];
            int rightScore = nums[right] - dp[left][right - 1];
            dp[left][right] = leftScore > rightScore ? leftScore : rightScore;
        }
    }
    bool result = dp[0][numsSize - 1] >= 0;
    for (int index = 0; index < numsSize; index++) {
        free(dp[index]);
    }
    free(dp);
    return result;
}
