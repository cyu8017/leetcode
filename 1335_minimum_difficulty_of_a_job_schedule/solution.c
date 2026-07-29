// LeetCode 1335 - Minimum Difficulty of a Job Schedule
// https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

#include <stdlib.h>

int minDifficulty(int* jobDifficulty, int jobDifficultySize, int d) {
    int n = jobDifficultySize;
    if (n < d) return -1;
    int INF = 1000000000;
    int* dp = (int*)malloc(n * sizeof(int));
    int hardest = 0;
    for (int i = 0; i < n; i++) {
        if (jobDifficulty[i] > hardest) hardest = jobDifficulty[i];
        dp[i] = hardest;
    }
    for (int day = 1; day < d; day++) {
        int* nxt = (int*)malloc(n * sizeof(int));
        for (int i = 0; i < n; i++) nxt[i] = INF;
        for (int end = day; end < n; end++) {
            hardest = 0;
            for (int start = end; start >= day; start--) {
                if (jobDifficulty[start] > hardest) hardest = jobDifficulty[start];
                int cand = dp[start - 1] + hardest;
                if (cand < nxt[end]) nxt[end] = cand;
            }
        }
        free(dp);
        dp = nxt;
    }
    int ans = dp[n - 1];
    free(dp);
    return ans;
}
