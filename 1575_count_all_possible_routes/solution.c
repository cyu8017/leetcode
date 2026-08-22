// LeetCode 1575 - Count All Possible Routes
// https://leetcode.com/problems/count-all-possible-routes/

#include <stdlib.h>

static const int MOD1575 = 1000000007;
static int* locs1575;
static int n1575, finish1575;
static int** memo1575;

static int dp1575(int city, int left) {
    if (memo1575[city][left] != -1) return memo1575[city][left];
    long long total = (city == finish1575);
    for (int nxt = 0; nxt < n1575; nxt++) {
        int cost = locs1575[city] - locs1575[nxt];
        if (cost < 0) cost = -cost;
        if (nxt != city && cost <= left) {
            total += dp1575(nxt, left - cost);
        }
    }
    return memo1575[city][left] = (int)(total % MOD1575);
}

int countRoutes(int* locations, int locationsSize, int start, int finish, int fuel) {
    locs1575 = locations;
    n1575 = locationsSize;
    finish1575 = finish;
    memo1575 = (int**)malloc((size_t)n1575 * sizeof(int*));
    for (int i = 0; i < n1575; i++) {
        memo1575[i] = (int*)malloc((size_t)(fuel + 1) * sizeof(int));
        for (int j = 0; j <= fuel; j++) memo1575[i][j] = -1;
    }
    int ans = dp1575(start, fuel);
    for (int i = 0; i < n1575; i++) free(memo1575[i]);
    free(memo1575);
    return ans;
}
