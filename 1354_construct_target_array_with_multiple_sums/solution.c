// LeetCode 1354 - Construct Target Array With Multiple Sums
// https://leetcode.com/problems/construct-target-array-with-multiple-sums/

#include <stdlib.h>
#include <stdbool.h>

typedef struct { long long* data; int size; int cap; } MaxHeap;
static void hpush(MaxHeap* h, long long v) {
    if (h->size == h->cap) { h->cap *= 2; h->data = (long long*)realloc(h->data, h->cap * sizeof(long long)); }
    int i = h->size++;
    h->data[i] = v;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h->data[p] >= h->data[i]) break;
        long long t = h->data[p]; h->data[p] = h->data[i]; h->data[i] = t; i = p;
    }
}
static long long hpop(MaxHeap* h) {
    long long res = h->data[0];
    h->data[0] = h->data[--h->size];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, s = i;
        if (l < h->size && h->data[l] > h->data[s]) s = l;
        if (r < h->size && h->data[r] > h->data[s]) s = r;
        if (s == i) break;
        long long t = h->data[i]; h->data[i] = h->data[s]; h->data[s] = t; i = s;
    }
    return res;
}

bool isPossible(int* target, int targetSize) {
    if (targetSize == 1) return target[0] == 1;
    MaxHeap h = { (long long*)malloc(targetSize * 2 * sizeof(long long)), 0, targetSize * 2 };
    long long total = 0;
    for (int i = 0; i < targetSize; i++) { total += target[i]; hpush(&h, target[i]); }
    while (1) {
        long long x = hpop(&h);
        long long rest = total - x;
        if (x == 1 || rest == 1) { free(h.data); return true; }
        if (rest == 0 || x <= rest) { free(h.data); return false; }
        long long prev = x % rest;
        if (prev == 0) { free(h.data); return false; }
        total = rest + prev;
        hpush(&h, prev);
    }
}
