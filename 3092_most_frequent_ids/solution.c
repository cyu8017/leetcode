// LeetCode 3092 - Most Frequent IDs
// https://leetcode.com/problems/most-frequent-ids/

#include <stdlib.h>
#include <stdbool.h>

typedef struct { int key, val; bool used; } HEnt;
static unsigned hash_u(unsigned x) { x ^= x >> 16; x *= 0x7feb352dU; x ^= x >> 15; x *= 0x846ca68bU; x ^= x >> 16; return x; }
static int hget(HEnt* t, int cap, int key) {
    unsigned h = hash_u((unsigned)key) & (unsigned)(cap - 1);
    while (t[h].used) { if (t[h].key == key) return t[h].val; h = (h + 1) & (unsigned)(cap - 1); }
    return 0;
}
static void hadd(HEnt* t, int cap, int key, int d) {
    unsigned h = hash_u((unsigned)key) & (unsigned)(cap - 1);
    while (t[h].used) {
        if (t[h].key == key) { t[h].val += d; return; }
        h = (h + 1) & (unsigned)(cap - 1);
    }
    t[h].used = true; t[h].key = key; t[h].val = d;
}
static void hset(HEnt* t, int cap, int key, int val) {
    unsigned h = hash_u((unsigned)key) & (unsigned)(cap - 1);
    while (t[h].used) {
        if (t[h].key == key) { t[h].val = val; return; }
        h = (h + 1) & (unsigned)(cap - 1);
    }
    t[h].used = true; t[h].key = key; t[h].val = val;
}

typedef struct { int* a; int n, cap; } MaxHeap;
static void mh_push(MaxHeap* h, int x) {
    if (h->n == h->cap) { h->cap = h->cap ? h->cap*2 : 16; h->a = (int*)realloc(h->a, (size_t)h->cap*sizeof(int)); }
    int i = h->n++; h->a[i] = x;
    while (i > 0) { int p=(i-1)/2; if (h->a[p] >= h->a[i]) break; int t=h->a[p]; h->a[p]=h->a[i]; h->a[i]=t; i=p; }
}
static void mh_pop(MaxHeap* h) {
    h->a[0] = h->a[--h->n];
    int i = 0;
    for (;;) {
        int l=2*i+1,r=2*i+2,m=i;
        if (l<h->n && h->a[l]>h->a[m]) m=l;
        if (r<h->n && h->a[r]>h->a[m]) m=r;
        if (m==i) break;
        int t=h->a[i]; h->a[i]=h->a[m]; h->a[m]=t; i=m;
    }
}

long long* mostFrequentIDs(int* nums, int numsSize, int* freq, int freqSize, int* returnSize) {
    (void)freqSize;
    int cap = 1; while (cap < numsSize * 4 + 16) cap <<= 1;
    HEnt* cnt = (HEnt*)calloc((size_t)cap, sizeof(HEnt));
    HEnt* lazy = (HEnt*)calloc((size_t)cap, sizeof(HEnt));
    MaxHeap pq = {NULL, 0, 0};
    long long* ans = (long long*)malloc((size_t)numsSize * sizeof(long long));
    for (int i = 0; i < numsSize; i++) {
        int x = nums[i], f = freq[i];
        int old = hget(cnt, cap, x);
        hadd(lazy, cap, old, 1);
        int nw = old + f;
        hset(cnt, cap, x, nw);
        mh_push(&pq, nw);
        while (pq.n > 0 && hget(lazy, cap, pq.a[0]) > 0) {
            hadd(lazy, cap, pq.a[0], -1);
            mh_pop(&pq);
        }
        ans[i] = pq.n > 0 ? pq.a[0] : 0;
    }
    free(cnt); free(lazy); free(pq.a);
    *returnSize = numsSize;
    return ans;
}
