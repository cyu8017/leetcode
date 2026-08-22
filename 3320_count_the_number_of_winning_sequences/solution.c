// LeetCode 3320 - Count the Number of Winning Sequences
// https://leetcode.com/problems/count-the-number-of-winning-sequences/

#include <stdlib.h>
#include <string.h>

int countWinningSequences(char* s) {
    const int mod = 1000000007;
    int n = (int)strlen(s);
    int mp[128]; mp['F']=0; mp['W']=1; mp['E']=2;
    int beat[3] = {2, 0, 1};
    int score[3][3];
    for (int a = 0; a < 3; a++)
        for (int b = 0; b < 3; b++) {
            if (a == b) score[a][b] = 0;
            else if (beat[a] == b) score[a][b] = 1;
            else score[a][b] = -1;
        }
    int offset = n;
    int* dp[3];
    for (int i = 0; i < 3; i++) dp[i] = (int*)calloc((size_t)(2 * n + 1), sizeof(int));
    int b0 = mp[(int)s[0]];
    for (int a = 0; a < 3; a++) dp[a][score[a][b0] + offset] = 1;
    for (int i = 1; i < n; i++) {
        int* ndp[3];
        for (int j = 0; j < 3; j++) ndp[j] = (int*)calloc((size_t)(2 * n + 1), sizeof(int));
        int b = mp[(int)s[i]];
        for (int last = 0; last < 3; last++) {
            for (int d = 0; d <= 2 * n; d++) {
                if (!dp[last][d]) continue;
                for (int a = 0; a < 3; a++) {
                    if (a == last) continue;
                    int nd = d + score[a][b];
                    if (nd < 0 || nd > 2 * n) continue;
                    ndp[a][nd] = (ndp[a][nd] + dp[last][d]) % mod;
                }
            }
        }
        for (int j = 0; j < 3; j++) { free(dp[j]); dp[j] = ndp[j]; }
    }
    int ans = 0;
    for (int a = 0; a < 3; a++)
        for (int d = offset + 1; d <= 2 * n; d++)
            ans = (ans + dp[a][d]) % mod;
    for (int i = 0; i < 3; i++) free(dp[i]);
    return ans;
}
