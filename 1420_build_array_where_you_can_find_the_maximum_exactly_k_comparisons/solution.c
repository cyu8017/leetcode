// LeetCode 1420 - Build Array Where You Can Find The Maximum Exactly K Comparisons
// https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/

#include <stdlib.h>
#include <string.h>

int numOfArrays(int n, int m, int k) {
    const int MOD = 1000000007;
    int* dp = (int*)calloc((k + 1) * (m + 1), sizeof(int));
    for (int maximum = 1; maximum <= m; maximum++) dp[1 * (m + 1) + maximum] = 1;
    for (int t = 1; t < n; t++) {
        int* nxt = (int*)calloc((k + 1) * (m + 1), sizeof(int));
        for (int cost = 1; cost <= k; cost++) {
            long long prefix = 0;
            for (int maximum = 1; maximum <= m; maximum++) {
                prefix = (prefix + dp[cost * (m + 1) + (maximum - 1)]) % MOD;
                nxt[cost * (m + 1) + maximum] = (int)(((long long)maximum * dp[cost * (m + 1) + maximum] + prefix) % MOD);
            }
        }
        free(dp); dp = nxt;
    }
    long long ans = 0;
    for (int maximum = 1; maximum <= m; maximum++) ans = (ans + dp[k * (m + 1) + maximum]) % MOD;
    free(dp);
    return (int)ans;
}
