// LeetCode 2209 - Minimum White Tiles After Covering With Carpets
// https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/

#include <stdlib.h>
#include <string.h>

int minimumWhiteTiles(char* floor, int numCarpets, int carpetLen) {
    int n = (int)strlen(floor);
    int** dp = (int**)malloc((size_t)(numCarpets + 1) * sizeof(int*));
    for (int i = 0; i <= numCarpets; i++) {
        dp[i] = (int*)malloc((size_t)(n + 1) * sizeof(int));
        for (int j = 0; j <= n; j++) dp[i][j] = 1 << 30;
    }
    dp[0][0] = 0;
    for (int j = 1; j <= n; j++) {
        dp[0][j] = dp[0][j - 1];
        if (floor[j - 1] == '1') dp[0][j]++;
    }
    for (int c = 1; c <= numCarpets; c++) {
        dp[c][0] = 0;
        for (int j = 1; j <= n; j++) {
            dp[c][j] = dp[c][j - 1];
            if (floor[j - 1] == '1') dp[c][j]++;
            int start = j - carpetLen;
            if (start < 0) start = 0;
            if (dp[c - 1][start] < dp[c][j]) dp[c][j] = dp[c - 1][start];
        }
    }
    int ans = dp[numCarpets][n];
    for (int i = 0; i <= numCarpets; i++) free(dp[i]);
    free(dp);
    return ans;
}
