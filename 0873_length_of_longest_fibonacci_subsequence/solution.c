// LeetCode 0873 - Length of Longest Fibonacci Subsequence
// https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

#include <stdlib.h>

#define MAX(a,b) ((a)>(b)?(a):(b))

int lenLongestFibSubseq(int* arr, int arrSize) {
    int n = arrSize;
    int** dp = (int**)malloc((size_t)n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        dp[i] = (int*)malloc((size_t)n * sizeof(int));
        for (int j = 0; j < n; j++) dp[i][j] = 2;
    }
    int ans = 0;
    for (int j = 0; j < n; j++) {
        for (int i = 0; i < j; i++) {
            int need = arr[j] - arr[i];
            int lo = 0, hi = i - 1, k = -1;
            while (lo <= hi) {
                int mid = (lo + hi) / 2;
                if (arr[mid] == need) { k = mid; break; }
                if (arr[mid] < need) lo = mid + 1;
                else hi = mid - 1;
            }
            if (k >= 0) {
                dp[i][j] = dp[k][i] + 1;
                ans = MAX(ans, dp[i][j]);
            }
        }
    }
    for (int i = 0; i < n; i++) free(dp[i]);
    free(dp);
    return ans >= 3 ? ans : 0;
}
