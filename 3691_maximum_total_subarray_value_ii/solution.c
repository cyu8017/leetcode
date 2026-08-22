// LeetCode 3691 - Maximum Total Subarray Value II
// https://leetcode.com/problems/maximum-total-subarray-value-ii/

#include <stdlib.h>

typedef struct {
    int n, maxLog;
    int** fMax;
    int** fMin;
    int* lg;
} SparseTable;

static int imax(int a, int b) { return a > b ? a : b; }
static int imin(int a, int b) { return a < b ? a : b; }

static SparseTable* newST(int* data, int n) {
    SparseTable* st = (SparseTable*)malloc(sizeof(SparseTable));
    int maxLog = 0;
    while ((1 << maxLog) <= n) maxLog++;
    maxLog++;
    st->n = n; st->maxLog = maxLog;
    st->fMax = (int**)malloc((size_t)n * sizeof(int*));
    st->fMin = (int**)malloc((size_t)n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        st->fMax[i] = (int*)calloc((size_t)maxLog, sizeof(int));
        st->fMin[i] = (int*)calloc((size_t)maxLog, sizeof(int));
        st->fMax[i][0] = data[i];
        st->fMin[i][0] = data[i];
    }
    st->lg = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 2; i <= n; i++) st->lg[i] = st->lg[i >> 1] + 1;
    for (int j = 1; j < maxLog; j++) {
        for (int i = 0; i <= n - (1 << j); i++) {
            st->fMax[i][j] = imax(st->fMax[i][j - 1], st->fMax[i + (1 << (j - 1))][j - 1]);
            st->fMin[i][j] = imin(st->fMin[i][j - 1], st->fMin[i + (1 << (j - 1))][j - 1]);
        }
    }
    return st;
}

static int qMax(SparseTable* st, int l, int r) {
    int k = st->lg[r - l + 1];
    return imax(st->fMax[l][k], st->fMax[r - (1 << k) + 1][k]);
}
static int qMin(SparseTable* st, int l, int r) {
    int k = st->lg[r - l + 1];
    return imin(st->fMin[l][k], st->fMin[r - (1 << k) + 1][k]);
}

static void freeST(SparseTable* st) {
    for (int i = 0; i < st->n; i++) { free(st->fMax[i]); free(st->fMin[i]); }
    free(st->fMax); free(st->fMin); free(st->lg); free(st);
}

typedef struct { long long val; int l, r; } Item;
typedef struct { Item* a; int n, cap; } MaxHeap;

static void hpPush(MaxHeap* h, Item it) {
    if (h->n == h->cap) { h->cap = h->cap ? h->cap * 2 : 16; h->a = (Item*)realloc(h->a, (size_t)h->cap * sizeof(Item)); }
    int i = h->n++;
    h->a[i] = it;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h->a[i].val <= h->a[p].val) break;
        Item t = h->a[i]; h->a[i] = h->a[p]; h->a[p] = t;
        i = p;
    }
}
static Item hpPop(MaxHeap* h) {
    Item top = h->a[0];
    h->a[0] = h->a[--h->n];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, b = i;
        if (l < h->n && h->a[l].val > h->a[b].val) b = l;
        if (r < h->n && h->a[r].val > h->a[b].val) b = r;
        if (b == i) break;
        Item t = h->a[i]; h->a[i] = h->a[b]; h->a[b] = t;
        i = b;
    }
    return top;
}

long long maxTotalValue(int* nums, int numsSize, int k) {
    int n = numsSize;
    SparseTable* st = newST(nums, n);
    MaxHeap pq = {0};
    for (int l = 0; l < n; l++) {
        long long val = (long long)qMax(st, l, n - 1) - qMin(st, l, n - 1);
        hpPush(&pq, (Item){val, l, n - 1});
    }
    long long ans = 0;
    for (int i = 0; i < k; i++) {
        Item curr = hpPop(&pq);
        ans += curr.val;
        if (curr.r > curr.l) {
            long long nextVal = (long long)qMax(st, curr.l, curr.r - 1) - qMin(st, curr.l, curr.r - 1);
            hpPush(&pq, (Item){nextVal, curr.l, curr.r - 1});
        }
    }
    free(pq.a);
    freeST(st);
    return ans;
}
