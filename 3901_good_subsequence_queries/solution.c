// LeetCode 3901 - Good Subsequence Queries
// https://leetcode.com/problems/good-subsequence-queries/

#include <stdlib.h>

static int gcd3901(int a, int b) {
    while (b) { int t = a % b; a = b; b = t; }
    return a;
}

typedef struct { int l, r, g; } Node3901;
typedef struct { Node3901* tr; } Seg3901;

static void build3901(Seg3901* st, int u, int l, int r) {
    st->tr[u].l = l; st->tr[u].r = r; st->tr[u].g = 0;
    if (l == r) return;
    int mid = (l + r) >> 1;
    build3901(st, u << 1, l, mid);
    build3901(st, u << 1 | 1, mid + 1, r);
}

static void pushup3901(Seg3901* st, int u) {
    st->tr[u].g = gcd3901(st->tr[u << 1].g, st->tr[u << 1 | 1].g);
}

static void modify3901(Seg3901* st, int u, int x, int v) {
    if (st->tr[u].l == st->tr[u].r) { st->tr[u].g = v; return; }
    int mid = (st->tr[u].l + st->tr[u].r) >> 1;
    if (x <= mid) modify3901(st, u << 1, x, v);
    else modify3901(st, u << 1 | 1, x, v);
    pushup3901(st, u);
}

static int query3901(Seg3901* st, int u, int l, int r) {
    if (l > r) return 0;
    if (st->tr[u].l >= l && st->tr[u].r <= r) return st->tr[u].g;
    int mid = (st->tr[u].l + st->tr[u].r) >> 1;
    if (r <= mid) return query3901(st, u << 1, l, r);
    if (l > mid) return query3901(st, u << 1 | 1, l, r);
    return gcd3901(query3901(st, u << 1, l, mid), query3901(st, u << 1 | 1, mid + 1, r));
}

int countGoodSubseq(int* nums, int numsSize, int p, int** queries, int queriesSize, int* queriesColSize) {
    (void)queriesColSize;
    int n = numsSize;
    Seg3901 st;
    st.tr = calloc((size_t)(n << 2), sizeof(Node3901));
    build3901(&st, 1, 1, n);
    int cnt = 0;
    for (int i = 0; i < n; i++) {
        if (nums[i] % p == 0) { modify3901(&st, 1, i + 1, nums[i]); cnt++; }
    }
    int ans = 0;
    for (int qi = 0; qi < queriesSize; qi++) {
        int idx = queries[qi][0], val = queries[qi][1];
        if (nums[idx] % p == 0) { modify3901(&st, 1, idx + 1, 0); cnt--; }
        if (val % p == 0) { modify3901(&st, 1, idx + 1, val); cnt++; }
        nums[idx] = val;
        if (st.tr[1].g != p) continue;
        if (cnt < n || n > 6) { ans++; continue; }
        for (int i = 1; i <= n; i++) {
            int leftG = query3901(&st, 1, 1, i - 1);
            int rightG = query3901(&st, 1, i + 1, n);
            if (gcd3901(leftG, rightG) == p) { ans++; break; }
        }
    }
    free(st.tr);
    return ans;
}
