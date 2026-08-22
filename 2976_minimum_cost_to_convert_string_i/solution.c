// LeetCode 2976 - Minimum Cost to Convert String I
// https://leetcode.com/problems/minimum-cost-to-convert-string-i/

#include <string.h>

long long minimumCost(char* source, char* target, char** original, int originalSize, char** changed, int changedSize, int* cost, int costSize) {
    (void)changedSize;
    (void)costSize;
    const long long INF = 1LL << 60;
    long long dist[26][26];
    for (int i = 0; i < 26; i++) {
        for (int j = 0; j < 26; j++) {
            dist[i][j] = (i == j) ? 0 : INF;
        }
    }
    for (int i = 0; i < originalSize; i++) {
        int u = original[i][0] - 'a';
        int v = changed[i][0] - 'a';
        long long w = cost[i];
        if (w < dist[u][v]) dist[u][v] = w;
    }
    for (int k = 0; k < 26; k++) {
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < 26; j++) {
                if (dist[i][k] + dist[k][j] < dist[i][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
    long long ans = 0;
    int n = (int)strlen(source);
    for (int i = 0; i < n; i++) {
        int a = source[i] - 'a', b = target[i] - 'a';
        if (dist[a][b] >= INF / 2) return -1;
        ans += dist[a][b];
    }
    return ans;
}
