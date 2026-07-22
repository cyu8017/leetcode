// LeetCode 1606 - Find Servers That Handled Most Number of Requests
// https://leetcode.com/problems/find-servers-that-handled-most-number-of-requests/

#include <stdlib.h>

typedef struct { long long freeAt; int server; } Busy;
typedef struct { int* data; int size; int cap; } IntHeap;
typedef struct { Busy* data; int size; int cap; } BusyHeap;

static void intEnsure(IntHeap* h) {
    if (h->size < h->cap) return;
    h->cap = h->cap ? h->cap * 2 : 16;
    h->data = (int*)realloc(h->data, (size_t)h->cap * sizeof(int));
}
static void intPush(IntHeap* h, int v) {
    intEnsure(h);
    int i = h->size++;
    h->data[i] = v;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h->data[p] <= h->data[i]) break;
        int t = h->data[p]; h->data[p] = h->data[i]; h->data[i] = t;
        i = p;
    }
}
static int intPop(IntHeap* h) {
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
static void busyEnsure(BusyHeap* h) {
    if (h->size < h->cap) return;
    h->cap = h->cap ? h->cap * 2 : 16;
    h->data = (Busy*)realloc(h->data, (size_t)h->cap * sizeof(Busy));
}
static void busyPush(BusyHeap* h, long long freeAt, int server) {
    busyEnsure(h);
    int i = h->size++;
    h->data[i].freeAt = freeAt; h->data[i].server = server;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h->data[p].freeAt <= h->data[i].freeAt) break;
        Busy t = h->data[p]; h->data[p] = h->data[i]; h->data[i] = t;
        i = p;
    }
}
static Busy busyPop(BusyHeap* h) {
    Busy top = h->data[0];
    h->data[0] = h->data[--h->size];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = l + 1, best = i;
        if (l < h->size && h->data[l].freeAt < h->data[best].freeAt) best = l;
        if (r < h->size && h->data[r].freeAt < h->data[best].freeAt) best = r;
        if (best == i) break;
        Busy t = h->data[i]; h->data[i] = h->data[best]; h->data[best] = t;
        i = best;
    }
    return top;
}

int* busiestServers(int k, int* arrival, int arrivalSize, int* load, int loadSize, int* returnSize) {
    (void)loadSize;
    IntHeap available = {0};
    BusyHeap busy = {0};
    int* count = (int*)calloc((size_t)k, sizeof(int));
    for (int i = 0; i < k; i++) intPush(&available, i);
    for (int i = 0; i < arrivalSize; i++) {
        long long t = arrival[i];
        while (busy.size && busy.data[0].freeAt <= t) {
            Busy b = busyPop(&busy);
            int adj = i + ((b.server - i) % k + k) % k;
            intPush(&available, adj);
        }
        if (!available.size) continue;
        int server = intPop(&available) % k;
        count[server]++;
        busyPush(&busy, t + load[i], server);
    }
    int best = 0;
    for (int i = 0; i < k; i++) if (count[i] > best) best = count[i];
    int* ans = (int*)malloc((size_t)k * sizeof(int));
    *returnSize = 0;
    for (int i = 0; i < k; i++) if (count[i] == best) ans[(*returnSize)++] = i;
    free(count); free(available.data); free(busy.data);
    return ans;
}
