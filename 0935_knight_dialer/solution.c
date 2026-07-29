// LeetCode 0935 - Knight Dialer
// https://leetcode.com/problems/knight-dialer/

int knightDialer(int n) {
    const int MOD = 1000000007;
    static const int moves[10][3] = {
        {4,6,-1},{6,8,-1},{7,9,-1},{4,8,-1},{0,3,9},
        {-1,-1,-1},{0,1,7},{2,6,-1},{1,3,-1},{2,4,-1}
    };
    static const int mcnt[10] = {2,2,2,2,3,0,3,2,2,2};
    long long dp[10];
    for (int i = 0; i < 10; i++) dp[i] = 1;
    for (int step = 1; step < n; step++) {
        long long ndp[10] = {0};
        for (int i = 0; i < 10; i++)
            for (int k = 0; k < mcnt[i]; k++)
                ndp[moves[i][k]] = (ndp[moves[i][k]] + dp[i]) % MOD;
        for (int i = 0; i < 10; i++) dp[i] = ndp[i];
    }
    long long ans = 0;
    for (int i = 0; i < 10; i++) ans = (ans + dp[i]) % MOD;
    return (int)ans;
}
