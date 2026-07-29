// LeetCode 1218 - Longest Arithmetic Subsequence of Given Difference
// https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

#include <stdlib.h>
#include <string.h>

int longestSubsequence(int* arr, int arrSize, int difference) {
    int offset = 20000;
    int size = 40001;
    int* dp = (int*)calloc((size_t)size, sizeof(int));
    int ans = 0;
    for (int i = 0; i < arrSize; i++) {
        int key = arr[i] + offset;
        int prev = arr[i] - difference + offset;
        dp[key] = (prev >= 0 && prev < size ? dp[prev] : 0) + 1;
        if (dp[key] > ans) ans = dp[key];
    }
    free(dp);
    return ans;
}
