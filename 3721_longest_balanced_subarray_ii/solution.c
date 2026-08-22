// LeetCode 3721 - Longest Balanced Subarray II
// https://leetcode.com/problems/longest-balanced-subarray-ii/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int l, r, mn, mx, lazy;
} Node;

typedef struct {
    Node* tr;
} SegmentTree;

static int imin(int a, int b) { return a < b ? a : b; }
static int imax(int a, int b) { return a > b ? a : b; }

static void apply(SegmentTree* st, int u, int v) {
    st->tr[u].mn += v;
    st->tr[u].mx += v;
    st->tr[u].lazy += v;
}

static void pushup(SegmentTree* st, int u) {
    st->tr[u].mn = imin(st->tr[u << 1].mn, st->tr[u << 1 | 1].mn);
    st->tr[u].mx = imax(st->tr[u << 1].mx, st->tr[u << 1 | 1].mx);
}

static void pushdown(SegmentTree* st, int u) {
    if (st->tr[u].lazy != 0) {
        int v = st->tr[u].lazy;
        apply(st, u << 1, v);
        apply(st, u << 1 | 1, v);
        st->tr[u].lazy = 0;
    }
}

static void build(SegmentTree* st, int u, int l, int r) {
    st->tr[u].l = l; st->tr[u].r = r;
    st->tr[u].mn = st->tr[u].mx = st->tr[u].lazy = 0;
    if (l == r) return;
    int mid = (l + r) >> 1;
    build(st, u << 1, l, mid);
    build(st, u << 1 | 1, mid + 1, r);
}

static void modify(SegmentTree* st, int u, int l, int r, int v) {
    if (st->tr[u].l >= l && st->tr[u].r <= r) { apply(st, u, v); return; }
    pushdown(st, u);
    int mid = (st->tr[u].l + st->tr[u].r) >> 1;
    if (l <= mid) modify(st, u << 1, l, r, v);
    if (r > mid) modify(st, u << 1 | 1, l, r, v);
    pushup(st, u);
}

static int query(SegmentTree* st, int u, int target) {
    if (st->tr[u].l == st->tr[u].r) return st->tr[u].l;
    pushdown(st, u);
    int left = u << 1, right = u << 1 | 1;
    if (st->tr[left].mn <= target && target <= st->tr[left].mx)
        return query(st, left, target);
    return query(st, right, target);
}

#define MAP_SIZE 200003
static int mk[MAP_SIZE], mv[MAP_SIZE];
static char mu[MAP_SIZE];
static void mc(void){memset(mu,0,sizeof(mu));}
static int* mp(int k){
    int i=(int)((unsigned)k%MAP_SIZE);
    while(mu[i]&&mk[i]!=k){if(++i==MAP_SIZE)i=0;}
    if(!mu[i]){mu[i]=1;mk[i]=k;mv[i]=0;}
    return &mv[i];
}
static int mhas(int k, int* out){
    int i=(int)((unsigned)k%MAP_SIZE);
    while(mu[i]&&mk[i]!=k){if(++i==MAP_SIZE)i=0;}
    if(!mu[i]) return 0;
    *out = mv[i]; return 1;
}

int longestBalanced(int* nums, int numsSize) {
    int n = numsSize;
    SegmentTree st;
    st.tr = (Node*)calloc((size_t)(n << 2) + 5, sizeof(Node));
    build(&st, 1, 0, n);
    mc();
    int now = 0, ans = 0;
    for (int i = 1; i <= n; i++) {
        int x = nums[i - 1];
        int det = (x & 1) ? 1 : -1;
        int pos;
        if (mhas(x, &pos)) {
            modify(&st, 1, pos, n, -det);
            now -= det;
        }
        *mp(x) = i;
        modify(&st, 1, i, n, det);
        now += det;
        pos = query(&st, 1, now);
        if (i - pos > ans) ans = i - pos;
    }
    free(st.tr);
    return ans;
}
