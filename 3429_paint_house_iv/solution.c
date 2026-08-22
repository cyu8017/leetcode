// LeetCode 3429 - Paint House IV
// https://leetcode.com/problems/paint-house-iv/

long long minCost(int n, int** cost, int costSize, int* costColSize) {
    (void)costSize; (void)costColSize;
    const long long INF = 1LL << 60;
    long long dp[3][3];
    for (int a = 0; a < 3; a++) for (int b = 0; b < 3; b++)
        dp[a][b] = a == b ? INF : (long long)cost[0][a] + cost[n - 1][b];
    int m = n / 2;
    for (int i = 1; i < m; i++) {
        long long ndp[3][3];
        for (int a = 0; a < 3; a++) for (int b = 0; b < 3; b++) ndp[a][b] = INF;
        for (int pa = 0; pa < 3; pa++) for (int pb = 0; pb < 3; pb++) {
            if (dp[pa][pb] >= INF) continue;
            for (int a = 0; a < 3; a++) if (a != pa)
                for (int b = 0; b < 3; b++) if (b != pb && a != b) {
                    long long v = dp[pa][pb] + cost[i][a] + cost[n - 1 - i][b];
                    if (v < ndp[a][b]) ndp[a][b] = v;
                }
        }
        for (int a = 0; a < 3; a++) for (int b = 0; b < 3; b++) dp[a][b] = ndp[a][b];
    }
    long long ans = INF;
    for (int a = 0; a < 3; a++) for (int b = 0; b < 3; b++) if (dp[a][b] < ans) ans = dp[a][b];
    return ans;
}
