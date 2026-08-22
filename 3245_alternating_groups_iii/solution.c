// LeetCode 3245 - Alternating Groups III
// https://leetcode.com/problems/alternating-groups-iii/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int n;
    int *counts;
    int *lengths;
} SegTree3245;

typedef struct { int l, r; } IKey;

static void stAddRec(SegTree3245 *st, int ti, int lo, int hi, int i, int val) {
    if (lo == hi) {
        st->counts[ti] += val;
        st->lengths[ti] = st->counts[ti] * i;
        return;
    }
    int mid = (lo + hi) / 2;
    if (i <= mid) stAddRec(st, 2 * ti + 1, lo, mid, i, val);
    else stAddRec(st, 2 * ti + 2, mid + 1, hi, i, val);
    st->counts[ti] = st->counts[2 * ti + 1] + st->counts[2 * ti + 2];
    st->lengths[ti] = st->lengths[2 * ti + 1] + st->lengths[2 * ti + 2];
}

static void stAdd(SegTree3245 *st, int i, int val) {
    stAddRec(st, 0, 0, st->n - 1, i, val);
}

static int stQuery(int *tree, int ti, int lo, int hi, int i, int j) {
    if (i <= lo && hi <= j) return tree[ti];
    if (j < lo || hi < i) return 0;
    int mid = (lo + hi) / 2;
    return stQuery(tree, ti * 2 + 1, lo, mid, i, j) + stQuery(tree, ti * 2 + 2, mid + 1, hi, i, j);
}

typedef struct {
    IKey *keys;
    int n, cap;
    SegTree3245 tree;
    int *arr;
    int N;
} Ctx3245;

static void insertI(Ctx3245 *c, int l, int r) {
    if (c->n == c->cap) {
        c->cap = c->cap ? c->cap * 2 : 16;
        c->keys = (IKey *)realloc(c->keys, (size_t)c->cap * sizeof(IKey));
    }
    c->keys[c->n++] = (IKey){l, r};
    if (l < c->N) stAdd(&c->tree, r - l + 1, 1);
}

static void removeI(Ctx3245 *c, int l, int r) {
    for (int i = 0; i < c->n; i++) {
        if (c->keys[i].l == l && c->keys[i].r == r) {
            c->keys[i] = c->keys[--c->n];
            break;
        }
    }
    if (l < c->N) stAdd(&c->tree, r - l + 1, -1);
}

static void findInterval(Ctx3245 *c, int target, int *bl, int *br) {
    *bl = -1; *br = -1;
    for (int i = 0; i < c->n; i++) {
        if (c->keys[i].l <= target && target <= c->keys[i].r) {
            if (c->keys[i].l > *bl) { *bl = c->keys[i].l; *br = c->keys[i].r; }
        }
    }
}

static int getNum(Ctx3245 *c, int sz) {
    int numIntervals = stQuery(c->tree.counts, 0, 0, c->tree.n - 1, sz, c->tree.n - 1);
    int sumIntervals = stQuery(c->tree.lengths, 0, 0, c->tree.n - 1, sz, c->tree.n - 1);
    int num = sumIntervals - numIntervals * sz + numIntervals;
    int l, r;
    findInterval(c, c->N, &l, &r);
    if (l < 0 || l >= c->N || r - l + 1 < sz) return num;
    if (r >= c->N) {
        int nonDup = c->N - l;
        int numGroups = (r - l + 1) - sz + 1;
        int extra = numGroups - nonDup;
        if (extra > 0) num -= extra;
    }
    return num;
}

static void update3245(Ctx3245 *c, int index, int color) {
    if (c->arr[index] == color) return;
    c->arr[index] = color;
    int start, end;
    findInterval(c, index, &start, &end);
    removeI(c, start, end);
    if (start < index && index < end) {
        insertI(c, start, index - 1);
        insertI(c, index, index);
        insertI(c, index + 1, end);
        return;
    }
    if (start == index && index < end) insertI(c, start + 1, end);
    if (start < index && index == end) insertI(c, start, end - 1);
    int ns = index, ne = index;
    for (;;) {
        int merged = 0;
        for (int i = 0; i < c->n; i++) {
            if (c->keys[i].r + 1 == ns && c->arr[c->keys[i].r] != c->arr[ns]) {
                int kl = c->keys[i].l, kr = c->keys[i].r;
                removeI(c, kl, kr);
                ns = kl;
                merged = 1;
                break;
            }
        }
        if (!merged) break;
    }
    for (;;) {
        int merged = 0;
        for (int i = 0; i < c->n; i++) {
            if (c->keys[i].l == ne + 1 && c->arr[c->keys[i].l] != c->arr[ne]) {
                int kl = c->keys[i].l, kr = c->keys[i].r;
                removeI(c, kl, kr);
                ne = kr;
                merged = 1;
                break;
            }
        }
        if (!merged) break;
    }
    insertI(c, ns, ne);
}

int* numberOfAlternatingGroups(int* colors, int colorsSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    (void)queriesColSize;
    int n = colorsSize;
    Ctx3245 c;
    memset(&c, 0, sizeof(c));
    c.N = n;
    c.arr = (int*)malloc((size_t)(2 * n - 1) * sizeof(int));
    for (int i = 0; i < n; i++) c.arr[i] = colors[i];
    for (int i = 0; i < n - 1; i++) c.arr[n + i] = colors[i];
    c.tree.n = 2 * n - 1;
    c.tree.counts = (int*)calloc((size_t)(4 * c.tree.n), sizeof(int));
    c.tree.lengths = (int*)calloc((size_t)(4 * c.tree.n), sizeof(int));
    int start = 0;
    for (int i = 1; i < 2 * n - 1; i++) {
        if (c.arr[i] == c.arr[i - 1]) {
            insertI(&c, start, i - 1);
            start = i;
        }
    }
    insertI(&c, start, 2 * n - 2);
    int* ans = (int*)malloc((size_t)queriesSize * sizeof(int));
    int alen = 0;
    for (int qi = 0; qi < queriesSize; qi++) {
        if (queries[qi][0] == 1) {
            ans[alen++] = getNum(&c, queries[qi][1]);
        } else {
            int index = queries[qi][1], color = queries[qi][2];
            if (c.arr[index] != color) {
                update3245(&c, index, color);
                if (index < n - 1) update3245(&c, index + n, color);
            }
        }
    }
    free(c.arr); free(c.tree.counts); free(c.tree.lengths); free(c.keys);
    *returnSize = alen;
    return ans;
}
