// LeetCode 2093 - Minimum Cost to Reach City With Discounts
// https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts/

#include <stdlib.h>
#include <limits.h>

typedef struct { int cost, city, disc; } Item2093;

typedef struct { Item2093* a; int n, cap; } PQ2093;

static void pqPush(PQ2093* p, Item2093 x) {
    if (p->n == p->cap) { p->cap *= 2; p->a = (Item2093*)realloc(p->a, (size_t)p->cap * sizeof(Item2093)); }
    int i = p->n++;
    p->a[i] = x;
    while (i > 0) {
        int par = (i - 1) / 2;
        if (p->a[par].cost <= p->a[i].cost) break;
        Item2093 t = p->a[par]; p->a[par] = p->a[i]; p->a[i] = t;
        i = par;
    }
}

static Item2093 pqPop(PQ2093* p) {
    Item2093 top = p->a[0];
    p->a[0] = p->a[--p->n];
    int i = 0;
    for (;;) {
        int l = 2 * i + 1, r = l + 1, sm = i;
        if (l < p->n && p->a[l].cost < p->a[sm].cost) sm = l;
        if (r < p->n && p->a[r].cost < p->a[sm].cost) sm = r;
        if (sm == i) break;
        Item2093 t = p->a[i]; p->a[i] = p->a[sm]; p->a[sm] = t;
        i = sm;
    }
    return top;
}

int minimumCost(int n, int** highways, int highwaysSize, int* highwaysColSize, int discounts) {
    (void)highwaysColSize;
    int* deg = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < highwaysSize; i++) { deg[highways[i][0]]++; deg[highways[i][1]]++; }
    int** g = (int**)malloc((size_t)n * sizeof(int*));
    int** gw = (int**)malloc((size_t)n * sizeof(int*));
    int* gc = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++) {
        g[i] = (int*)malloc((size_t)(deg[i] ? deg[i] : 1) * sizeof(int));
        gw[i] = (int*)malloc((size_t)(deg[i] ? deg[i] : 1) * sizeof(int));
    }
    for (int i = 0; i < highwaysSize; i++) {
        int a = highways[i][0], b = highways[i][1], w = highways[i][2];
        g[a][gc[a]] = b; gw[a][gc[a]++] = w;
        g[b][gc[b]] = a; gw[b][gc[b]++] = w;
    }
    int** dist = (int**)malloc((size_t)n * sizeof(int*));
    for (int i = 0; i < n; i++) {
        dist[i] = (int*)malloc((size_t)(discounts + 1) * sizeof(int));
        for (int j = 0; j <= discounts; j++) dist[i][j] = INT_MAX / 4;
    }
    PQ2093 pq = {0};
    pq.cap = 64;
    pq.a = (Item2093*)malloc((size_t)pq.cap * sizeof(Item2093));
    pqPush(&pq, (Item2093){0, 0, discounts});
    dist[0][discounts] = 0;
    int ans = -1;
    while (pq.n > 0) {
        Item2093 cur = pqPop(&pq);
        if (cur.city == n - 1) { ans = cur.cost; break; }
        if (cur.cost > dist[cur.city][cur.disc]) continue;
        for (int i = 0; i < gc[cur.city]; i++) {
            int v = g[cur.city][i], w = gw[cur.city][i];
            if (cur.cost + w < dist[v][cur.disc]) {
                dist[v][cur.disc] = cur.cost + w;
                pqPush(&pq, (Item2093){dist[v][cur.disc], v, cur.disc});
            }
            if (cur.disc > 0 && cur.cost + w / 2 < dist[v][cur.disc - 1]) {
                dist[v][cur.disc - 1] = cur.cost + w / 2;
                pqPush(&pq, (Item2093){dist[v][cur.disc - 1], v, cur.disc - 1});
            }
        }
    }
    for (int i = 0; i < n; i++) { free(g[i]); free(gw[i]); free(dist[i]); }
    free(g); free(gw); free(gc); free(deg); free(dist); free(pq.a);
    return ans;
}
