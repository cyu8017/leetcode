// LeetCode 1786 - Number of Restricted Paths From First to Last Node
// https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/

#include <stdlib.h>

typedef struct {
    long long dist;
    int node;
} HeapItem;

static void heapPush(HeapItem* heap, int* size, long long dist, int node) {
    int i = (*size)++;
    heap[i].dist = dist;
    heap[i].node = node;
    while (i > 0) {
        int parent = (i - 1) / 2;
        if (heap[parent].dist <= heap[i].dist) {
            break;
        }
        HeapItem tmp = heap[parent];
        heap[parent] = heap[i];
        heap[i] = tmp;
        i = parent;
    }
}

static HeapItem heapPop(HeapItem* heap, int* size) {
    HeapItem top = heap[0];
    heap[0] = heap[--(*size)];
    int i = 0;
    for (;;) {
        int smallest = i;
        int l = 2 * i + 1;
        int r = 2 * i + 2;
        if (l < *size && heap[l].dist < heap[smallest].dist) smallest = l;
        if (r < *size && heap[r].dist < heap[smallest].dist) smallest = r;
        if (smallest == i) break;
        HeapItem tmp = heap[smallest];
        heap[smallest] = heap[i];
        heap[i] = tmp;
        i = smallest;
    }
    return top;
}

static int cmpHeapItem(const void* a, const void* b) {
    const HeapItem* x = (const HeapItem*)a;
    const HeapItem* y = (const HeapItem*)b;
    if (x->dist < y->dist) return -1;
    if (x->dist > y->dist) return 1;
    return 0;
}

int countRestrictedPaths(int n, int** edges, int edgesSize, int* edgesColSize) {
    int* degree = (int*)calloc(n + 1, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        degree[edges[i][0]]++;
        degree[edges[i][1]]++;
    }
    int* start = (int*)malloc((n + 2) * sizeof(int));
    start[0] = 0;
    start[1] = 0;
    for (int u = 1; u <= n; u++) {
        start[u + 1] = start[u] + degree[u];
    }
    int total = start[n + 1];
    int* adjNode = (int*)malloc(total * sizeof(int));
    int* adjWeight = (int*)malloc(total * sizeof(int));
    int* fill = (int*)malloc((n + 1) * sizeof(int));
    for (int u = 1; u <= n; u++) {
        fill[u] = start[u];
    }
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0];
        int b = edges[i][1];
        int w = edges[i][2];
        adjNode[fill[a]] = b;
        adjWeight[fill[a]] = w;
        fill[a]++;
        adjNode[fill[b]] = a;
        adjWeight[fill[b]] = w;
        fill[b]++;
    }
    const long long INF = 0x3f3f3f3f3f3f3f3fLL;
    long long* dist = (long long*)malloc((n + 1) * sizeof(long long));
    for (int u = 0; u <= n; u++) {
        dist[u] = INF;
    }
    dist[n] = 0;
    HeapItem* heap = (HeapItem*)malloc((total + 1) * sizeof(HeapItem));
    int heapSize = 0;
    heapPush(heap, &heapSize, 0, n);
    while (heapSize > 0) {
        HeapItem top = heapPop(heap, &heapSize);
        long long d = top.dist;
        int u = top.node;
        if (d != dist[u]) {
            continue;
        }
        for (int idx = start[u]; idx < start[u + 1]; idx++) {
            int v = adjNode[idx];
            long long nd = d + adjWeight[idx];
            if (nd < dist[v]) {
                dist[v] = nd;
                heapPush(heap, &heapSize, nd, v);
            }
        }
    }
    HeapItem* order = (HeapItem*)malloc(n * sizeof(HeapItem));
    for (int u = 1; u <= n; u++) {
        order[u - 1].dist = dist[u];
        order[u - 1].node = u;
    }
    qsort(order, n, sizeof(HeapItem), cmpHeapItem);
    const long long MOD = 1000000007;
    long long* cnt = (long long*)calloc(n + 1, sizeof(long long));
    cnt[n] = 1;
    for (int i = 0; i < n; i++) {
        int u = order[i].node;
        if (u == n) {
            continue;
        }
        for (int idx = start[u]; idx < start[u + 1]; idx++) {
            int v = adjNode[idx];
            if (dist[u] > dist[v]) {
                cnt[u] = (cnt[u] + cnt[v]) % MOD;
            }
        }
    }
    int ans = (int)cnt[1];
    free(degree);
    free(start);
    free(adjNode);
    free(adjWeight);
    free(fill);
    free(dist);
    free(heap);
    free(order);
    free(cnt);
    return ans;
}
