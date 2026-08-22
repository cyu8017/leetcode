// LeetCode 2767 - Partition String Into Minimum Beautiful Substrings
// https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/

#include <string.h>
#include <stdlib.h>

int minimumBeautifulSubstrings(char* s) {
    int n = (int)strlen(s);
    char pow5[20][20];
    int pcnt = 0;
    long long x = 1;
    while (1) {
        // binary of x
        char buf[64];
        int len = 0;
        long long t = x;
        if (t == 0) { buf[len++] = '0'; }
        else {
            char tmp[64]; int tl = 0;
            while (t) { tmp[tl++] = (char)('0' + (t & 1)); t >>= 1; }
            for (int i = tl - 1; i >= 0; i--) buf[len++] = tmp[i];
        }
        buf[len] = 0;
        if (len > n) break;
        strcpy(pow5[pcnt++], buf);
        if (x > (1LL << 40) / 5) break;
        x *= 5;
    }
    const int INF = 1 << 30;
    int* dp = (int*)malloc((n + 1) * sizeof(int));
    for (int i = 0; i <= n; i++) dp[i] = INF;
    dp[0] = 0;
    for (int i = 0; i < n; i++) {
        if (dp[i] == INF || s[i] == '0') continue;
        for (int j = i + 1; j <= n; j++) {
            int len = j - i;
            for (int p = 0; p < pcnt; p++) {
                if ((int)strlen(pow5[p]) == len && strncmp(s + i, pow5[p], len) == 0) {
                    if (dp[i] + 1 < dp[j]) dp[j] = dp[i] + 1;
                }
            }
        }
    }
    int ans = dp[n] == INF ? -1 : dp[n];
    free(dp);
    return ans;
}
