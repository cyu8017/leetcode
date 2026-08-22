// LeetCode 3547 - Maximum Sum of Edge Values in a Graph
// https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/

#include <stdlib.h>

static int cmp_desc(const void* a, const void* b) {
    int x = *(const int*)a, y = *(const int*)b;
    return (y > x) - (y < x);
}

static long long calc_score(int left, int right, int isCycle) {
    int w0 = right, w1 = right;
    long long score = 0;
    for (int value = right - 1; value >= left; value--) {
        score += (long long)w0 * value;
        int nw0 = w1, nw1 = value;
        w0 = nw0;
        w1 = nw1;
    }
    if (isCycle) score += (long long)w0 * w1;
    return score;
}

long long maxScore(int n, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    int** g = (int**)calloc((size_t)n, sizeof(int*));
    int* gsz = (int*)calloc((size_t)n, sizeof(int));
    int* gcap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        for (int rep = 0; rep < 2; rep++) {
            int a = rep ? v : u, b = rep ? u : v;
            if (gsz[a] == gcap[a]) {
                gcap[a] = gcap[a] ? gcap[a] * 2 : 2;
                g[a] = (int*)realloc(g[a], (size_t)gcap[a] * sizeof(int));
            }
            g[a][gsz[a]++] = b;
        }
    }
    char* seen = (char*)calloc((size_t)n, 1);
    int* cycleSizes = (int*)malloc((size_t)n * sizeof(int));
    int* pathSizes = (int*)malloc((size_t)n * sizeof(int));
    int cc = 0, pc = 0;
    for (int i = 0; i < n; i++) {
        if (seen[i]) continue;
        int* comp = (int*)malloc((size_t)n * sizeof(int));
        int cn = 0;
        comp[cn++] = i;
        seen[i] = 1;
        for (int qi = 0; qi < cn; qi++) {
            int u = comp[qi];
            for (int j = 0; j < gsz[u]; j++) {
                int v = g[u][j];
                if (!seen[v]) { seen[v] = 1; comp[cn++] = v; }
            }
        }
        int allDeg2 = 1;
        for (int j = 0; j < cn; j++) if (gsz[comp[j]] != 2) { allDeg2 = 0; break; }
        if (allDeg2) cycleSizes[cc++] = cn;
        else if (cn > 1) pathSizes[pc++] = cn;
        free(comp);
    }
    long long ans = 0;
    int curN = n;
    for (int i = 0; i < cc; i++) {
        ans += calc_score(curN - cycleSizes[i] + 1, curN, 1);
        curN -= cycleSizes[i];
    }
    qsort(pathSizes, (size_t)pc, sizeof(int), cmp_desc);
    for (int i = 0; i < pc; i++) {
        ans += calc_score(curN - pathSizes[i] + 1, curN, 0);
        curN -= pathSizes[i];
    }
    for (int i = 0; i < n; i++) free(g[i]);
    free(g); free(gsz); free(gcap); free(seen); free(cycleSizes); free(pathSizes);
    return ans;
}
