// LeetCode 1353 - Maximum Number of Events That Can Be Attended
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

#include <stdlib.h>

static int cmp_events(const void* a, const void* b) {
    int* x = *(int**)a;
    int* y = *(int**)b;
    return x[0] - y[0];
}

typedef struct { int* data; int size; int cap; } MinHeap;
static void heap_push(MinHeap* h, int v) {
    if (h->size == h->cap) { h->cap *= 2; h->data = (int*)realloc(h->data, h->cap * sizeof(int)); }
    int i = h->size++;
    h->data[i] = v;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h->data[p] <= h->data[i]) break;
        int t = h->data[p]; h->data[p] = h->data[i]; h->data[i] = t; i = p;
    }
}
static int heap_pop(MinHeap* h) {
    int res = h->data[0];
    h->data[0] = h->data[--h->size];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, s = i;
        if (l < h->size && h->data[l] < h->data[s]) s = l;
        if (r < h->size && h->data[r] < h->data[s]) s = r;
        if (s == i) break;
        int t = h->data[i]; h->data[i] = h->data[s]; h->data[s] = t; i = s;
    }
    return res;
}

int maxEvents(int** events, int eventsSize, int* eventsColSize) {
    (void)eventsColSize;
    qsort(events, eventsSize, sizeof(int*), cmp_events);
    MinHeap h = { (int*)malloc(16 * sizeof(int)), 0, 16 };
    int i = 0, ans = 0, day = 0;
    while (i < eventsSize || h.size) {
        if (!h.size) day = events[i][0] > day ? events[i][0] : day;
        while (i < eventsSize && events[i][0] <= day) {
            heap_push(&h, events[i][1]);
            i++;
        }
        while (h.size && h.data[0] < day) heap_pop(&h);
        if (h.size) { heap_pop(&h); ans++; day++; }
    }
    free(h.data);
    return ans;
}
