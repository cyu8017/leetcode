// LeetCode 2386 - Find the K-Sum of an Array
// https://leetcode.com/problems/find-the-k-sum-of-an-array/

#include <stdlib.h>

typedef struct { long long sum; int i; } Pair;
typedef struct { Pair* data; int size; int cap; } PQ;

static void pqPush(PQ* h, Pair p) {
    if (h->size >= h->cap) { h->cap = h->cap ? h->cap * 2 : 8; h->data = (Pair*)realloc(h->data, (size_t)h->cap * sizeof(Pair)); }
    int i = h->size++;
    h->data[i] = p;
    while (i > 0) {
        int par = (i - 1) / 2;
        if (h->data[par].sum >= h->data[i].sum) break;
        Pair t = h->data[par]; h->data[par] = h->data[i]; h->data[i] = t;
        i = par;
    }
}

static Pair pqPop(PQ* h) {
    Pair res = h->data[0];
    h->data[0] = h->data[--h->size];
    int i = 0;
    while (1) {
        int l = 2*i+1, r = 2*i+2, best = i;
        if (l < h->size && h->data[l].sum > h->data[best].sum) best = l;
        if (r < h->size && h->data[r].sum > h->data[best].sum) best = r;
        if (best == i) break;
        Pair t = h->data[i]; h->data[i] = h->data[best]; h->data[best] = t;
        i = best;
    }
    return res;
}

static int cmpInt(const void* a, const void* b) { return *(const int*)a - *(const int*)b; }

long long kSum(int* nums, int numsSize, int k) {
    long long total = 0;
    int* absNums = (int*)malloc((size_t)numsSize * sizeof(int));
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] >= 0) { total += nums[i]; absNums[i] = nums[i]; }
        else absNums[i] = -nums[i];
    }
    qsort(absNums, (size_t)numsSize, sizeof(int), cmpInt);
    PQ h = {0};
    pqPush(&h, (Pair){total, 0});
    for (int t = 0; t < k - 1; t++) {
        Pair cur = pqPop(&h);
        if (cur.i >= numsSize) continue;
        pqPush(&h, (Pair){cur.sum - absNums[cur.i], cur.i + 1});
        if (cur.i > 0)
            pqPush(&h, (Pair){cur.sum - absNums[cur.i] + absNums[cur.i - 1], cur.i + 1});
    }
    long long ans = h.data[0].sum;
    free(h.data); free(absNums);
    return ans;
}
