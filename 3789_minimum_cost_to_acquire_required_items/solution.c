// LeetCode 3789 - Minimum Cost To Acquire Required Items
// https://leetcode.com/problems/minimum-cost-to-acquire-required-items/

long long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
    long long a = (long long)need1 * cost1 + (long long)need2 * cost2;
    int mx = need1 > need2 ? need1 : need2;
    long long b = (long long)costBoth * mx;
    int mn = need1 < need2 ? need1 : need2;
    long long c = (long long)costBoth * mn + (long long)(need1 - mn) * cost1 + (long long)(need2 - mn) * cost2;
    long long ans = a < b ? a : b;
    if (c < ans) ans = c;
    return ans;
}
