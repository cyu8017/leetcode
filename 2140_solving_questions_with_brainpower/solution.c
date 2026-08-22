// LeetCode 2140 - Solving Questions With Brainpower
// https://leetcode.com/problems/solving-questions-with-brainpower/

#include <stdlib.h>

long long mostPoints(int** questions, int questionsSize, int* questionsColSize) {
    (void)questionsColSize;
    int n = questionsSize;
    long long* dp = (long long*)calloc((size_t)n + 1, sizeof(long long));
    for (int i = n - 1; i >= 0; i--) {
        int pts = questions[i][0], brain = questions[i][1];
        int next = i + brain + 1;
        long long take = pts;
        if (next < n) take += dp[next];
        dp[i] = dp[i + 1] > take ? dp[i + 1] : take;
    }
    long long ans = dp[0];
    free(dp);
    return ans;
}
