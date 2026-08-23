// LeetCode 4004 - Minimum Moves To Balance Circular Array II
// https://leetcode.com/problems/minimum-moves-to-balance-circular-array-ii/

#include <stdlib.h>
#include <string.h>
#include <stdint.h>

#define INF4004 1000000000

typedef struct {
    int to, cap, cost, rev;
} Edge4004;

typedef struct {
    Edge4004* a;
    int n, cap;
} Adj4004;

static void addEdge4004(Adj4004* g, int u, int v, int cap, int cost) {
    if (g[u].n == g[u].cap) {
        g[u].cap = g[u].cap ? g[u].cap * 2 : 4;
        g[u].a = (Edge4004*)realloc(g[u].a, (size_t)g[u].cap * sizeof(Edge4004));
    }
    if (g[v].n == g[v].cap) {
        g[v].cap = g[v].cap ? g[v].cap * 2 : 4;
        g[v].a = (Edge4004*)realloc(g[v].a, (size_t)g[v].cap * sizeof(Edge4004));
    }
    int ru = g[v].n, rv = g[u].n;
    g[u].a[g[u].n++] = (Edge4004){v, cap, cost, ru};
    g[v].a[g[v].n++] = (Edge4004){u, 0, -cost, rv};
}

static int64_t minCostFlow4004(Adj4004* g, int N, int source, int sink, int maxFlow) {
    int64_t totalCost = 0;
    int currentFlow = 0;
    int* dist = (int*)malloc((size_t)N * sizeof(int));
    int* parentNode = (int*)malloc((size_t)N * sizeof(int));
    int* parentEdge = (int*)malloc((size_t)N * sizeof(int));
    int* inQueue = (int*)malloc((size_t)N * sizeof(int));
    int* queue = (int*)malloc((size_t)(N * N + 16) * sizeof(int));

    while (currentFlow < maxFlow) {
        for (int i = 0; i < N; i++) {
            dist[i] = INF4004;
            parentNode[i] = -1;
            parentEdge[i] = -1;
            inQueue[i] = 0;
        }
        int head = 0, tail = 0;
        queue[tail++] = source;
        dist[source] = 0;
        inQueue[source] = 1;
        while (head < tail) {
            int u = queue[head++];
            inQueue[u] = 0;
            for (int i = 0; i < g[u].n; i++) {
                Edge4004* e = &g[u].a[i];
                if (e->cap > 0 && dist[e->to] > dist[u] + e->cost) {
                    dist[e->to] = dist[u] + e->cost;
                    parentNode[e->to] = u;
                    parentEdge[e->to] = i;
                    if (!inQueue[e->to]) {
                        inQueue[e->to] = 1;
                        queue[tail++] = e->to;
                    }
                }
            }
        }
        if (dist[sink] == INF4004) {
            totalCost = -1;
            break;
        }
        int pushFlow = maxFlow - currentFlow;
        for (int cur = sink; cur != source; cur = parentNode[cur]) {
            Edge4004* e = &g[parentNode[cur]].a[parentEdge[cur]];
            if (e->cap < pushFlow) pushFlow = e->cap;
        }
        for (int cur = sink; cur != source; cur = parentNode[cur]) {
            int p = parentNode[cur];
            int idx = parentEdge[cur];
            int rev = g[p].a[idx].rev;
            g[p].a[idx].cap -= pushFlow;
            g[cur].a[rev].cap += pushFlow;
        }
        currentFlow += pushFlow;
        totalCost += (int64_t)pushFlow * dist[sink];
    }

    free(dist);
    free(parentNode);
    free(parentEdge);
    free(inQueue);
    free(queue);
    return totalCost;
}

long long minMoves(int* balance, int balanceSize) {
    int totalBalance = 0, totalDeficit = 0;
    for (int i = 0; i < balanceSize; i++) {
        totalBalance += balance[i];
        if (balance[i] < 0) totalDeficit += -balance[i];
    }
    if (totalBalance < 0) return -1;
    if (totalDeficit == 0) return 0;

    int n = balanceSize;
    int source = n, sink = n + 1, N = n + 2;
    Adj4004* g = (Adj4004*)calloc((size_t)N, sizeof(Adj4004));

    for (int i = 0; i < n; i++) {
        int x = balance[i];
        if (x > 0) addEdge4004(g, source, i, x, 0);
        else if (x < 0) addEdge4004(g, i, sink, -x, 0);
        addEdge4004(g, i, (i + 1) % n, INF4004, 1);
        addEdge4004(g, i, (i - 1 + n) % n, INF4004, 1);
    }

    int64_t ans = minCostFlow4004(g, N, source, sink, totalDeficit);
    for (int i = 0; i < N; i++) free(g[i].a);
    free(g);
    return ans;
}
