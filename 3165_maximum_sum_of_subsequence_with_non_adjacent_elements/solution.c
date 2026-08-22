// LeetCode 3165 - Maximum Sum of Subsequence With Non-adjacent Elements
// https://leetcode.com/problems/maximum-sum-of-subsequence-with-non-adjacent-elements/

#include <stdlib.h>

typedef struct { int l, r, s00, s01, s10, s11; } Node3165;
static Node3165* tr3165;

static int max3165(int a, int b) { return a > b ? a : b; }

static void build3165(int u, int l, int r) {
    tr3165[u] = (Node3165){l, r, 0, 0, 0, 0};
    if (l == r) return;
    int mid = (l + r) >> 1;
    build3165(u << 1, l, mid);
    build3165(u << 1 | 1, mid + 1, r);
}

static void pushup3165(int u) {
    Node3165* L = &tr3165[u << 1];
    Node3165* R = &tr3165[u << 1 | 1];
    tr3165[u].s00 = max3165(L->s00 + R->s10, L->s01 + R->s00);
    tr3165[u].s01 = max3165(L->s00 + R->s11, L->s01 + R->s01);
    tr3165[u].s10 = max3165(L->s10 + R->s10, L->s11 + R->s00);
    tr3165[u].s11 = max3165(L->s10 + R->s11, L->s11 + R->s01);
}

static void modify3165(int u, int x, int v) {
    if (tr3165[u].l == tr3165[u].r) {
        tr3165[u].s11 = max3165(0, v);
        return;
    }
    int mid = (tr3165[u].l + tr3165[u].r) >> 1;
    if (x <= mid) modify3165(u << 1, x, v);
    else modify3165(u << 1 | 1, x, v);
    pushup3165(u);
}

static int query3165(int u, int l, int r) {
    if (tr3165[u].l >= l && tr3165[u].r <= r) return tr3165[u].s11;
    int mid = (tr3165[u].l + tr3165[u].r) >> 1;
    int ans = 0;
    if (r <= mid) ans = query3165(u << 1, l, r);
    if (l > mid) {
        int t = query3165(u << 1 | 1, l, r);
        if (t > ans) ans = t;
    }
    return ans;
}

int maximumSumSubsequence(int* nums, int numsSize, int** queries, int queriesSize, int* queriesColSize) {
    (void)queriesColSize;
    tr3165 = calloc(numsSize * 4 + 5, sizeof(Node3165));
    build3165(1, 1, numsSize);
    for (int i = 0; i < numsSize; i++) modify3165(1, i + 1, nums[i]);
    const int mod = 1000000007;
    int ans = 0;
    for (int i = 0; i < queriesSize; i++) {
        modify3165(1, queries[i][0] + 1, queries[i][1]);
        ans = (ans + query3165(1, 1, numsSize)) % mod;
    }
    free(tr3165);
    return ans;
}
