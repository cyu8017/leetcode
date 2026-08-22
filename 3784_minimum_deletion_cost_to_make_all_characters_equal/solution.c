// LeetCode 3784 - Minimum Deletion Cost To Make All Characters Equal
// https://leetcode.com/problems/minimum-deletion-cost-to-make-all-characters-equal/

#include <string.h>

long long minCost(char* s, int* cost, int costSize) {
    long long tot = 0;
    long long g[256] = {0};
    int n = costSize;
    for (int i = 0; i < n; i++) {
        tot += cost[i];
        g[(unsigned char)s[i]] += cost[i];
    }
    long long ans = tot;
    for (int i = 0; i < 256; i++) {
        if (g[i] && tot - g[i] < ans) ans = tot - g[i];
    }
    return ans;
}
