// LeetCode 0375 - Guess Number Higher or Lower II
// https://leetcode.com/problems/guess-number-higher-or-lower-ii/

#include <limits.h>
#include <stdlib.h>

int getMoneyAmount(int n) {
    int size = n + 2;
    int** dp = (int**)malloc((size_t)size * sizeof(int*));
    for (int index = 0; index < size; index++) {
        dp[index] = (int*)calloc((size_t)size, sizeof(int));
    }

    for (int length = 2; length <= n; length++) {
        for (int left = 1; left <= n - length + 1; left++) {
            int right = left + length - 1;
            dp[left][right] = INT_MAX;
            for (int guess = left; guess < right; guess++) {
                int cost = guess;
                int lower = dp[left][guess - 1];
                int upper = dp[guess + 1][right];
                if (lower > upper) {
                    cost += lower;
                } else {
                    cost += upper;
                }
                if (cost < dp[left][right]) {
                    dp[left][right] = cost;
                }
            }
        }
    }

    int result = dp[1][n];
    for (int index = 0; index < size; index++) {
        free(dp[index]);
    }
    free(dp);
    return result;
}
