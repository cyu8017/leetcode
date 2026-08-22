// LeetCode 2407 - Longest Increasing Subsequence II
// https://leetcode.com/problems/longest-increasing-subsequence-ii/

#include <stdlib.h>

typedef struct { int n; int* tree; } SegTree;

static void stUpdate(SegTree* st, int idx, int l, int r, int pos, int val) {
    if (l == r) { if (val > st->tree[idx]) st->tree[idx] = val; return; }
    int mid = (l + r) / 2;
    if (pos <= mid) stUpdate(st, idx * 2, l, mid, pos, val);
    else stUpdate(st, idx * 2 + 1, mid + 1, r, pos, val);
    int a = st->tree[idx * 2], b = st->tree[idx * 2 + 1];
    st->tree[idx] = a > b ? a : b;
}

static int stQuery(SegTree* st, int idx, int l, int r, int ql, int qr) {
    if (qr < l || r < ql) return 0;
    if (ql <= l && r <= qr) return st->tree[idx];
    int mid = (l + r) / 2;
    int a = stQuery(st, idx * 2, l, mid, ql, qr);
    int b = stQuery(st, idx * 2 + 1, mid + 1, r, ql, qr);
    return a > b ? a : b;
}

int lengthOfLIS(int* nums, int numsSize, int k) {
    int maxV = 0;
    for (int i = 0; i < numsSize; i++) if (nums[i] > maxV) maxV = nums[i];
    SegTree st; st.n = maxV + 1; st.tree = (int*)calloc((size_t)(4 * st.n), sizeof(int));
    int ans = 0;
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i];
        int lo = x - k; if (lo < 1) lo = 1;
        int best = 1;
        if (lo <= x - 1) best = stQuery(&st, 1, 1, maxV, lo, x - 1) + 1;
        stUpdate(&st, 1, 1, maxV, x, best);
        if (best > ans) ans = best;
    }
    free(st.tree);
    return ans;
}
