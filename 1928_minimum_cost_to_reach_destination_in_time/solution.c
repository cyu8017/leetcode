// LeetCode 1928 - Minimum Cost to Reach Destination in Time
// https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/

#include <stdlib.h>
#include <limits.h>

typedef struct { int cost, time, node; } Item;

static void push(Item** heap, int* sz, int* cap, Item v) {
    if (*sz >= *cap) {
        *cap = *cap ? *cap * 2 : 16;
        *heap = (Item*)realloc(*heap, (size_t)(*cap) * sizeof(Item));
    }
    int i = (*sz)++;
    (*heap)[i] = v;
    while (i > 0) {
        int p = (i - 1) / 2;
        if ((*heap)[p].cost <= (*heap)[i].cost) break;
        Item t = (*heap)[p]; (*heap)[p] = (*heap)[i]; (*heap)[i] = t;
        i = p;
    }
}

static Item pop(Item* heap, int* sz) {
    Item top = heap[0];
    heap[0] = heap[--(*sz)];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, best = i;
        if (l < *sz && heap[l].cost < heap[best].cost) best = l;
        if (r < *sz && heap[r].cost < heap[best].cost) best = r;
        if (best == i) break;
        Item t = heap[i]; heap[i] = heap[best]; heap[best] = t;
        i = best;
    }
    return top;
}

int minCost(int maxTime, int** edges, int edgesSize, int* edgesColSize, int* passingFee, int passingFeeSize) {
    (void)edgesColSize;
    int n = passingFeeSize;
    int** to = (int**)calloc((size_t)n, sizeof(int*));
    int** wt = (int**)calloc((size_t)n, sizeof(int*));
    int* deg = (int*)calloc((size_t)n, sizeof(int));
    int* cap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1], t = edges[i][2];
        for (int rep = 0; rep < 2; rep++) {
            if (deg[u] == cap[u]) {
                cap[u] = cap[u] ? cap[u] * 2 : 4;
                to[u] = (int*)realloc(to[u], (size_t)cap[u] * sizeof(int));
                wt[u] = (int*)realloc(wt[u], (size_t)cap[u] * sizeof(int));
            }
            to[u][deg[u]] = v;
            wt[u][deg[u]] = t;
            deg[u]++;
            int tmp = u; u = v; v = tmp;
        }
    }
    int* minTime = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) minTime[i] = maxTime + 1;
    Item* heap = NULL;
    int hsz = 0, hcap = 0;
    push(&heap, &hsz, &hcap, (Item){passingFee[0], 0, 0});
    int ans = -1;
    while (hsz) {
        Item cur = pop(heap, &hsz);
        if (cur.time >= minTime[cur.node]) continue;
        minTime[cur.node] = cur.time;
        if (cur.node == n - 1) { ans = cur.cost; break; }
        for (int i = 0; i < deg[cur.node]; i++) {
            int v = to[cur.node][i];
            int nt = cur.time + wt[cur.node][i];
            if (nt <= maxTime && nt < minTime[v]) {
                push(&heap, &hsz, &hcap, (Item){cur.cost + passingFee[v], nt, v});
            }
        }
    }
    for (int i = 0; i < n; i++) { free(to[i]); free(wt[i]); }
    free(to); free(wt); free(deg); free(cap); free(minTime); free(heap);
    return ans;
}
