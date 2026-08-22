// LeetCode 2305 - Fair Distribution of Cookies
// https://leetcode.com/problems/fair-distribution-of-cookies/

#include <stdlib.h>
#include <stdbool.h>

static void dfs_cookies(int i, int n, int k, int* cookies, int* bags, int* ans) {
    if (i == n) {
        int mx = 0;
        for (int j = 0; j < k; j++) if (bags[j] > mx) mx = bags[j];
        if (mx < *ans) *ans = mx;
        return;
    }
    bool seen[100]; // bags values up to large - use linear scan instead
    for (int j = 0; j < k; j++) {
        bool skip = false;
        for (int t = 0; t < j; t++) {
            if (bags[t] == bags[j]) { skip = true; break; }
        }
        if (skip) continue;
        bags[j] += cookies[i];
        if (bags[j] < *ans) dfs_cookies(i + 1, n, k, cookies, bags, ans);
        bags[j] -= cookies[i];
        if (bags[j] == 0) break;
    }
    (void)seen;
}

int distributeCookies(int* cookies, int cookiesSize, int k) {
    int* bags = (int*)calloc((size_t)k, sizeof(int));
    int ans = 1 << 30;
    dfs_cookies(0, cookiesSize, k, cookies, bags, &ans);
    free(bags);
    return ans;
}
