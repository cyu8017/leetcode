// LeetCode 3747 - Count Distinct Integers After Removing Zeros
// https://leetcode.com/problems/count-distinct-integers-after-removing-zeros/

#include <stdio.h>
#include <string.h>

static char s[32];
static int m;
static long long memo[20][2][2][2];
static char vis[20][2][2][2];

static long long dfs(int i, int zero, int lead, int limit) {
    if (i == m) return (zero == 0 && lead == 0) ? 1 : 0;
    if (!limit && vis[i][zero][lead][limit]) return memo[i][zero][lead][limit];
    int up = limit ? s[i] - '0' : 9;
    long long ans = 0;
    for (int d = 0; d <= up; d++) {
        int nxtZero = zero;
        if (d == 0 && lead == 0) nxtZero = 1;
        int nxtLead = (lead == 1 && d == 0) ? 1 : 0;
        int nxtLimit = (limit == 1 && d == up) ? 1 : 0;
        ans += dfs(i + 1, nxtZero, nxtLead, nxtLimit);
    }
    if (!limit) { vis[i][zero][lead][limit] = 1; memo[i][zero][lead][limit] = ans; }
    return ans;
}

long long countDistinct(long long n) {
    sprintf(s, "%lld", n);
    m = (int)strlen(s);
    memset(vis, 0, sizeof(vis));
    return dfs(0, 0, 1, 1);
}
