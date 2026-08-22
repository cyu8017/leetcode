// LeetCode 3977 - Minimum Time to Reach Target With Limited Power
// https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/

#include <stdlib.h>
#include <string.h>

typedef struct {
    long long d;
    int p; /* stored negated remaining power for heap order */
    int u;
} State3977;

typedef struct {
    State3977* a;
    int n, cap;
} PQ3977;

static void pqPush(PQ3977* pq, State3977 s) {
    if (pq->n == pq->cap) {
        pq->cap = pq->cap ? pq->cap * 2 : 64;
        pq->a = (State3977*)realloc(pq->a, (size_t)pq->cap * sizeof(State3977));
    }
    int i = pq->n++;
    pq->a[i] = s;
    while (i > 0) {
        int p = (i - 1) / 2;
        State3977* A = &pq->a[i];
        State3977* B = &pq->a[p];
        int better = (A->d < B->d) || (A->d == B->d && A->p < B->p);
        if (!better) break;
        State3977 tmp = *A; *A = *B; *B = tmp;
        i = p;
    }
}

static State3977 pqPop(PQ3977* pq) {
    State3977 top = pq->a[0];
    pq->a[0] = pq->a[--pq->n];
    int i = 0;
    for (;;) {
        int l = 2 * i + 1, r = l + 1, best = i;
        if (l < pq->n) {
            State3977* A = &pq->a[l];
            State3977* B = &pq->a[best];
            if (A->d < B->d || (A->d == B->d && A->p < B->p)) best = l;
        }
        if (r < pq->n) {
            State3977* A = &pq->a[r];
            State3977* B = &pq->a[best];
            if (A->d < B->d || (A->d == B->d && A->p < B->p)) best = r;
        }
        if (best == i) break;
        State3977 tmp = pq->a[i]; pq->a[i] = pq->a[best]; pq->a[best] = tmp;
        i = best;
    }
    return top;
}

typedef struct { int v, t; } Edge3977;
typedef struct { Edge3977* a; int n, cap; } Adj3977;

static void adjPush(Adj3977* g, int v, int t) {
    if (g->n == g->cap) {
        g->cap = g->cap ? g->cap * 2 : 4;
        g->a = (Edge3977*)realloc(g->a, (size_t)g->cap * sizeof(Edge3977));
    }
    g->a[g->n].v = v;
    g->a[g->n].t = t;
    g->n++;
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
long long* minTimeMaxPower(int n, int** edges, int edgesSize, int* edgesColSize, int power, int* cost, int costSize,
                           int source, int target, int* returnSize) {
    (void)edgesColSize;
    (void)costSize;
    const long long INF = 1LL << 62;
    Adj3977* g = (Adj3977*)calloc((size_t)n, sizeof(Adj3977));
    for (int i = 0; i < edgesSize; i++) {
        adjPush(&g[edges[i][0]], edges[i][1], edges[i][2]);
    }

    long long* dist = (long long*)malloc((size_t)n * (size_t)(power + 1) * sizeof(long long));
    for (int i = 0; i < n * (power + 1); i++) dist[i] = INF;

    PQ3977 pq = {0};
    State3977 start = {0, -power, source};
    pqPush(&pq, start);
    dist[source * (power + 1) + power] = 0;

    long long* ans = (long long*)malloc(2 * sizeof(long long));
    ans[0] = -1;
    ans[1] = -1;

    while (pq.n > 0) {
        State3977 cur = pqPop(&pq);
        long long d = cur.d;
        int p = -cur.p;
        int u = cur.u;
        if (u == target) {
            ans[0] = d;
            ans[1] = p;
            break;
        }
        if (d > dist[u * (power + 1) + p] || p < cost[u]) continue;
        p -= cost[u];
        for (int i = 0; i < g[u].n; i++) {
            int v = g[u].a[i].v;
            int t = g[u].a[i].t;
            long long nd = d + t;
            int idx = v * (power + 1) + p;
            if (nd < dist[idx]) {
                dist[idx] = nd;
                State3977 nxt = {nd, -p, v};
                pqPush(&pq, nxt);
            }
        }
    }

    for (int i = 0; i < n; i++) free(g[i].a);
    free(g);
    free(dist);
    free(pq.a);
    *returnSize = 2;
    return ans;
}
