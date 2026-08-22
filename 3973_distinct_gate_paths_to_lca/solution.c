// LeetCode 3973 - Distinct Gate Paths to LCA
// https://leetcode.com/problems/distinct-gate-paths-to-lca/

#include <stdlib.h>
#include <string.h>

enum { MOD3973 = 1000000007LL };

typedef struct { long long m[2][2]; } Mat3973;

static Mat3973 mul3973(Mat3973 a, Mat3973 b) {
    Mat3973 c = {{{0}}};
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
            for (int k = 0; k < 2; k++)
                c.m[i][j] = (c.m[i][j] + a.m[i][k] * b.m[k][j]) % MOD3973;
    return c;
}

int gatePathXor(int n, int* parent, int parentSize, int** gates, int gatesSize, int* gatesColSize, int** queries, int queriesSize, int* queriesColSize) {
    (void)parentSize; (void)gatesSize; (void)gatesColSize; (void)queriesColSize;
    int logn = 1;
    while ((1 << logn) <= n) logn++;
    int** up = malloc((size_t)logn * sizeof(int*));
    Mat3973** product = malloc((size_t)logn * sizeof(Mat3973*));
    for (int level = 0; level < logn; level++) {
        up[level] = calloc((size_t)n, sizeof(int));
        product[level] = calloc((size_t)n, sizeof(Mat3973));
    }
    int** children = calloc((size_t)n, sizeof(int*));
    int* deg = calloc((size_t)n, sizeof(int));
    int* cap = calloc((size_t)n, sizeof(int));
    for (int node = 1; node < n; node++) {
        int p = parent[node];
        if (deg[p] == cap[p]) { cap[p] = cap[p] ? cap[p]*2 : 4; children[p] = realloc(children[p], (size_t)cap[p]*sizeof(int)); }
        children[p][deg[p]++] = node;
    }
    int* depth = calloc((size_t)n, sizeof(int));
    int* order = malloc((size_t)n * sizeof(int));
    int on = 0;
    order[on++] = 0;
    for (int i = 0; i < on; i++) {
        int u = order[i];
        for (int j = 0; j < deg[u]; j++) {
            int v = children[u][j];
            depth[v] = depth[u] + 1;
            order[on++] = v;
        }
    }
    for (int u = 0; u < n; u++) {
        up[0][u] = (u == 0) ? 0 : parent[u];
        product[0][u] = (Mat3973){{{gates[u][1], gates[u][2]}, {gates[u][2], gates[u][0]}}};
    }
    for (int level = 1; level < logn; level++) {
        for (int u = 0; u < n; u++) {
            int mid = up[level - 1][u];
            up[level][u] = up[level - 1][mid];
            product[level][u] = mul3973(product[level - 1][u], product[level - 1][mid]);
        }
    }
int answer = 0;
    for (int qi = 0; qi < queriesSize; qi++) {
        int a = queries[qi][0], cardA = queries[qi][1], b = queries[qi][2], cardB = queries[qi][3];
        /* LCA */
        int aa = a, bb = b;
        if (depth[aa] > depth[bb]) {
            int dist = depth[aa] - depth[bb];
            for (int level = 0; dist > 0; level++) { if (dist & 1) aa = up[level][aa]; dist >>= 1; }
        } else if (depth[bb] > depth[aa]) {
            int dist = depth[bb] - depth[aa];
            for (int level = 0; dist > 0; level++) { if (dist & 1) bb = up[level][bb]; dist >>= 1; }
        }
        if (aa != bb) {
            for (int level = logn - 1; level >= 0; level--) {
                if (up[level][aa] != up[level][bb]) { aa = up[level][aa]; bb = up[level][bb]; }
            }
            aa = up[0][aa];
        }
        int ancestor = aa;
        /* ways */
        long long vec[2] = {0, 0};
        vec[cardA] = 1;
        int node = a;
        int distance = depth[a] - depth[ancestor];
        for (int level = 0; distance > 0; level++) {
            if (distance & 1) {
                Mat3973 matrix = product[level][node];
                long long n0 = (vec[0] * matrix.m[0][0] + vec[1] * matrix.m[1][0]) % MOD3973;
                long long n1 = (vec[0] * matrix.m[0][1] + vec[1] * matrix.m[1][1]) % MOD3973;
                vec[0] = n0; vec[1] = n1;
                node = up[level][node];
            }
            distance >>= 1;
        }
        long long alice = (vec[0] + vec[1]) % MOD3973;
        vec[0] = vec[1] = 0; vec[cardB] = 1;
        node = b;
        distance = depth[b] - depth[ancestor];
        for (int level = 0; distance > 0; level++) {
            if (distance & 1) {
                Mat3973 matrix = product[level][node];
                long long n0 = (vec[0] * matrix.m[0][0] + vec[1] * matrix.m[1][0]) % MOD3973;
                long long n1 = (vec[0] * matrix.m[0][1] + vec[1] * matrix.m[1][1]) % MOD3973;
                vec[0] = n0; vec[1] = n1;
                node = up[level][node];
            }
            distance >>= 1;
        }
        long long bob = (vec[0] + vec[1]) % MOD3973;
        int total = (int)(alice * bob % MOD3973);
        answer ^= total;
    }
    for (int i = 0; i < logn; i++) { free(up[i]); free(product[i]); }
    for (int i = 0; i < n; i++) free(children[i]);
    free(up); free(product); free(children); free(deg); free(cap); free(depth); free(order);
    return answer;
}
