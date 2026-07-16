// LeetCode 0312 - Burst Balloons
// https://leetcode.com/problems/burst-balloons/

#include <stdlib.h>

static int maxInt(int left, int right) {
    return left > right ? left : right;
}

int maxCoins(int* nums, int numsSize) {
    int size = numsSize + 2;
    int* balloons = (int*)malloc((size_t)size * sizeof(int));
    balloons[0] = 1;
    for (int index = 0; index < numsSize; index++) {
        balloons[index + 1] = nums[index];
    }
    balloons[size - 1] = 1;

    int** dp = (int**)malloc((size_t)size * sizeof(int*));
    for (int row = 0; row < size; row++) {
        dp[row] = (int*)calloc((size_t)size, sizeof(int));
    }

    for (int length = 3; length <= size; length++) {
        for (int left = 0; left <= size - length; left++) {
            int right = left + length - 1;
            for (int mid = left + 1; mid < right; mid++) {
                int coins = dp[left][mid]
                    + dp[mid][right]
                    + balloons[left] * balloons[mid] * balloons[right];
                dp[left][right] = maxInt(dp[left][right], coins);
            }
        }
    }

    int answer = dp[0][size - 1];
    for (int row = 0; row < size; row++) {
        free(dp[row]);
    }
    free(dp);
    free(balloons);
    return answer;
}
