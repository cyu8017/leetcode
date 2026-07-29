// LeetCode 0964 - Least Operators to Express Number
// https://leetcode.com/problems/least-operators-to-express-number/

static int xg;

static int dfs(int t) {
    if (xg > t) {
        int a = 2 * t - 1, b = 2 * (xg - t);
        return a < b ? a : b;
    }
    if (xg == t) return 0;
    long long prod = xg;
    int n = 0;
    while (prod < t) { prod *= xg; n++; }
    if (prod == t) return n;
    int ans = dfs((int)(t - prod / xg)) + n;
    if (prod < 2LL * t) {
        int alt = dfs((int)(prod - t)) + n + 1;
        if (alt < ans) ans = alt;
    }
    return ans;
}

int leastOpsExpressTarget(int x, int target) {
    xg = x;
    return dfs(target);
}
