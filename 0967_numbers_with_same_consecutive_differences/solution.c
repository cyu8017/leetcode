// LeetCode 0967 - Numbers With Same Consecutive Differences
// https://leetcode.com/problems/numbers-with-same-consecutive-differences/

#include <stdlib.h>

static int* ans;
static int an, n_g, k_g;

static void dfs(int num, int length) {
    if (length == n_g) { ans[an++] = num; return; }
    int last = num % 10;
    int cands[2] = {last + k_g, last - k_g};
    int used0 = 0;
    for (int t = 0; t < 2; t++) {
        int nxt = cands[t];
        if (k_g == 0 && t == 1) continue;
        if (nxt >= 0 && nxt <= 9) dfs(num * 10 + nxt, length + 1);
    }
}

int* numsSameConsecDiff(int n, int k, int* returnSize) {
    n_g = n; k_g = k;
    ans = (int*)malloc(10000 * sizeof(int));
    an = 0;
    for (int start = 1; start <= 9; start++) dfs(start, 1);
    *returnSize = an;
    return ans;
}
