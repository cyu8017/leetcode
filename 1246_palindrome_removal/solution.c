// LeetCode 1246 - Palindrome Removal
// https://leetcode.com/problems/palindrome-removal/

#include <stdlib.h>

int minimumMoves(int* arr, int arrSize) {
    int** dp = (int**)malloc((size_t)arrSize * sizeof(int*));
    for (int i = 0; i < arrSize; i++) {
        dp[i] = (int*)malloc((size_t)arrSize * sizeof(int));
        dp[i][i] = 1;
    }
    for (int length = 2; length <= arrSize; length++) {
        for (int i = 0; i + length <= arrSize; i++) {
            int j = i + length - 1;
            dp[i][j] = 1 + dp[i + 1][j];
            if (arr[i] == arr[i + 1]) {
                int val = (i + 2 <= j) ? dp[i + 2][j] : 0;
                if (1 + val < dp[i][j]) dp[i][j] = 1 + val;
            }
            for (int k = i + 2; k <= j; k++) {
                if (arr[i] == arr[k]) {
                    int left = (i + 1 <= k - 1) ? dp[i + 1][k - 1] : 0;
                    int right = (k < j) ? dp[k + 1][j] : 0;
                    if (left + right < dp[i][j]) dp[i][j] = left + right;
                }
            }
        }
    }
    int ans = dp[0][arrSize - 1];
    for (int i = 0; i < arrSize; i++) free(dp[i]);
    free(dp);
    return ans;
}
