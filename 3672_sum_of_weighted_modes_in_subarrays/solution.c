// LeetCode 3672 - Sum of Weighted Modes in Subarrays
// https://leetcode.com/problems/sum-of-weighted-modes-in-subarrays/

#include <stdlib.h>
#include <string.h>

typedef struct { int freq, val; } Pair;

typedef struct {
    Pair* a;
    int n, cap;
} MaxHeap;

static void heapPush(MaxHeap* h, Pair p) {
    if (h->n == h->cap) {
        h->cap = h->cap ? h->cap * 2 : 16;
        h->a = (Pair*)realloc(h->a, (size_t)h->cap * sizeof(Pair));
    }
    int i = h->n++;
    h->a[i] = p;
    while (i > 0) {
        int pidx = (i - 1) / 2;
        Pair* x = &h->a[i]; Pair* y = &h->a[pidx];
        int better = (x->freq > y->freq) || (x->freq == y->freq && x->val < y->val);
        if (!better) break;
        Pair tmp = *x; *x = *y; *y = tmp;
        i = pidx;
    }
}

static void heapPop(MaxHeap* h) {
    h->a[0] = h->a[--h->n];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, best = i;
        if (l < h->n) {
            Pair* a = &h->a[l]; Pair* b = &h->a[best];
            if (a->freq > b->freq || (a->freq == b->freq && a->val < b->val)) best = l;
        }
        if (r < h->n) {
            Pair* a = &h->a[r]; Pair* b = &h->a[best];
            if (a->freq > b->freq || (a->freq == b->freq && a->val < b->val)) best = r;
        }
        if (best == i) break;
        Pair tmp = h->a[i]; h->a[i] = h->a[best]; h->a[best] = tmp;
        i = best;
    }
}

#define MAP_SIZE 200003
static int mapKey[MAP_SIZE];
static int mapVal[MAP_SIZE];
static char mapUsed[MAP_SIZE];

static void mapClear(void) { memset(mapUsed, 0, sizeof(mapUsed)); }

static int mapHash(int k) { return (int)((unsigned)k % MAP_SIZE); }

static int* mapGetPtr(int k) {
    int i = mapHash(k);
    while (mapUsed[i] && mapKey[i] != k) { if (++i == MAP_SIZE) i = 0; }
    if (!mapUsed[i]) { mapUsed[i] = 1; mapKey[i] = k; mapVal[i] = 0; }
    return &mapVal[i];
}

static int mapGet(int k) {
    int i = mapHash(k);
    while (mapUsed[i] && mapKey[i] != k) { if (++i == MAP_SIZE) i = 0; }
    return mapUsed[i] ? mapVal[i] : 0;
}

static long long getMode(MaxHeap* pq) {
    while (1) {
        Pair top = pq->a[0];
        if (mapGet(top.val) == top.freq) return (long long)top.freq * top.val;
        heapPop(pq);
    }
}

long long modeWeight(int* nums, int numsSize, int k) {
    mapClear();
    MaxHeap pq = {0};
    for (int i = 0; i < k; i++) {
        int x = nums[i];
        int* c = mapGetPtr(x);
        (*c)++;
        heapPush(&pq, (Pair){*c, x});
    }
    long long ans = getMode(&pq);
    for (int i = k; i < numsSize; i++) {
        int x = nums[i], y = nums[i - k];
        int* cx = mapGetPtr(x); (*cx)++;
        int* cy = mapGetPtr(y); (*cy)--;
        heapPush(&pq, (Pair){*cx, x});
        heapPush(&pq, (Pair){*cy, y});
        ans += getMode(&pq);
    }
    free(pq.a);
    return ans;
}
