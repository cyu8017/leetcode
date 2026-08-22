// LeetCode 3544 - Subtree Inversion Sum
// https://leetcode.com/problems/subtree-inversion-sum/

#include <stdlib.h>
#include <string.h>

static int **g3544, *gsz3544, *parent3544, *nums3544, k3544, n3544;
static long long *memo3544;
static char *seen3544;

static int key3544(int u, int steps, int inv) {
    return (u * (k3544 + 1) + steps) * 2 + inv;
}

static long long dp3544(int u, int steps, int inv) {
    int key = key3544(u, steps, inv);
    if (seen3544[key]) return memo3544[key];
    long long num = nums3544[u];
    if (inv) num = -num;
    long long negNum = -num;
    for (int i = 0; i < gsz3544[u]; i++) {
        int v = g3544[u][i];
        if (v == parent3544[u]) continue;
        parent3544[v] = u;
        int ns = steps + 1;
        if (ns > k3544) ns = k3544;
        num += dp3544(v, ns, inv);
        if (steps == k3544) negNum += dp3544(v, 1, !inv);
    }
    long long res = num;
    if (steps == k3544 && negNum > res) res = negNum;
    seen3544[key] = 1;
    memo3544[key] = res;
    return res;
}

long long subtreeInversionSum(int** edges, int edgesSize, int* edgesColSize, int* nums, int numsSize, int k) {
    (void)edgesColSize;
    n3544 = numsSize; k3544 = k; nums3544 = nums;
    g3544 = (int**)calloc((size_t)n3544, sizeof(int*));
    gsz3544 = (int*)calloc((size_t)n3544, sizeof(int));
    int* gcap = (int*)calloc((size_t)n3544, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        for (int rep = 0; rep < 2; rep++) {
            int a = rep ? v : u, b = rep ? u : v;
            if (gsz3544[a] == gcap[a]) {
                gcap[a] = gcap[a] ? gcap[a] * 2 : 2;
                g3544[a] = realloc(g3544[a], (size_t)gcap[a] * sizeof(int));
            }
            g3544[a][gsz3544[a]++] = b;
        }
    }
    parent3544 = (int*)malloc((size_t)n3544 * sizeof(int));
    for (int i = 0; i < n3544; i++) parent3544[i] = -1;
    int msz = n3544 * (k + 1) * 2;
    memo3544 = (long long*)calloc((size_t)msz, sizeof(long long));
    seen3544 = (char*)calloc((size_t)msz, 1);
    long long ans = dp3544(0, k, 0);
    for (int i = 0; i < n3544; i++) free(g3544[i]);
    free(g3544); free(gsz3544); free(gcap); free(parent3544); free(memo3544); free(seen3544);
    return ans;
}
