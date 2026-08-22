// LeetCode 2992 - Number of Self-Divisible Permutations
// https://leetcode.com/problems/number-of-self-divisible-permutations/

#include <stdbool.h>
#include <string.h>

static void dfs2992(int pos, int n, bool* used, int* ans) {
    if (pos > n) {
        (*ans)++;
        return;
    }
    for (int v = 1; v <= n; v++) {
        if (used[v]) continue;
        if (v % pos != 0 && pos % v != 0) continue;
        used[v] = true;
        dfs2992(pos + 1, n, used, ans);
        used[v] = false;
    }
}

int selfDivisiblePermutationCount(int n) {
    bool used[16];
    memset(used, 0, sizeof(used));
    int ans = 0;
    dfs2992(1, n, used, &ans);
    return ans;
}
