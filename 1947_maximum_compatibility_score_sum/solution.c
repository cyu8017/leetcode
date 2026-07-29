// LeetCode 1947 - Maximum Compatibility Score Sum
// https://leetcode.com/problems/maximum-compatibility-score-sum/

#include <stdlib.h>
#include <string.h>

int maxCompatibilitySum(int** students, int studentsSize, int* studentsColSize, int** mentors, int mentorsSize, int* mentorsColSize) {
    (void)mentorsSize; (void)mentorsColSize;
    int m = studentsSize, n = studentsColSize[0];
    int score[8][8];
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < m; j++) {
            int s = 0;
            for (int k = 0; k < n; k++) if (students[i][k] == mentors[j][k]) s++;
            score[i][j] = s;
        }
    }
    int N = 1 << m;
    int* dp = (int*)malloc((size_t)N * sizeof(int));
    for (int i = 0; i < N; i++) dp[i] = -1;
    dp[0] = 0;
    for (int mask = 0; mask < N; mask++) {
        if (dp[mask] < 0) continue;
        int i = 0, tmp = mask;
        while (tmp) { i += tmp & 1; tmp >>= 1; }
        if (i >= m) continue;
        for (int j = 0; j < m; j++) {
            if (mask & (1 << j)) continue;
            int nmask = mask | (1 << j);
            int val = dp[mask] + score[i][j];
            if (val > dp[nmask]) dp[nmask] = val;
        }
    }
    int ans = dp[N - 1];
    free(dp);
    return ans;
}
