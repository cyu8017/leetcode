// LeetCode 1642 - Furthest Building You Can Reach
// https://leetcode.com/problems/furthest-building-you-can-reach/

#include <stdlib.h>

typedef struct { int* data; int size; int cap; } MinHeap;

static void ensure(MinHeap* h) {
    if (h->size < h->cap) return;
    h->cap = h->cap ? h->cap * 2 : 16;
    h->data = (int*)realloc(h->data, (size_t)h->cap * sizeof(int));
}
static void push(MinHeap* h, int v) {
    ensure(h);
    int i = h->size++;
    h->data[i] = v;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h->data[p] <= h->data[i]) break;
        int t = h->data[p]; h->data[p] = h->data[i]; h->data[i] = t;
        i = p;
    }
}
static int pop(MinHeap* h) {
    int top = h->data[0];
    h->data[0] = h->data[--h->size];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = l + 1, best = i;
        if (l < h->size && h->data[l] < h->data[best]) best = l;
        if (r < h->size && h->data[r] < h->data[best]) best = r;
        if (best == i) break;
        int t = h->data[i]; h->data[i] = h->data[best]; h->data[best] = t;
        i = best;
    }
    return top;
}

int furthestBuilding(int* heights, int heightsSize, int bricks, int ladders) {
    MinHeap climbs = {0};
    for (int i = 0; i < heightsSize - 1; i++) {
        int d = heights[i + 1] - heights[i];
        if (d <= 0) continue;
        push(&climbs, d);
        if (climbs.size > ladders) bricks -= pop(&climbs);
        if (bricks < 0) {
            free(climbs.data);
            return i;
        }
    }
    free(climbs.data);
    return heightsSize - 1;
}
