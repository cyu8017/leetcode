// LeetCode 3864 - Minimum Cost To Partition A Binary String
// https://leetcode.com/problems/minimum-cost-to-partition-a-binary-string/

#include <stdlib.h>
#include <string.h>

static int* pre3864;
static int enc3864, flat3864;

static long long dfs3864(int l, int r) {
    int x = pre3864[r] - pre3864[l];
    long long res;
    if (x != 0) res = (long long)(r - l) * x * enc3864;
    else res = flat3864;
    if ((r - l) % 2 == 0) {
        int m = (l + r) / 2;
        long long cand = dfs3864(l, m) + dfs3864(m, r);
        if (cand < res) res = cand;
    }
    return res;
}

long long minCost(char* s, int encCost, int flatCost) {
    int n = (int)strlen(s);
    pre3864 = (int*)calloc((size_t)n + 1, sizeof(int));
    for (int i = 1; i <= n; i++) pre3864[i] = pre3864[i - 1] + (s[i - 1] - '0');
    enc3864 = encCost; flat3864 = flatCost;
    long long ans = dfs3864(0, n);
    free(pre3864);
    return ans;
}
