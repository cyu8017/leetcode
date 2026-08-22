// LeetCode 2508 - Add Edges to Make Degrees of All Nodes Even
// https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

static int cap2508;
static long long* keys2508;
static char* used2508;

static int hasEdge2508(int x, int y) {
    long long a = x < y ? ((long long)x << 20) | y : ((long long)y << 20) | x;
    unsigned h = (unsigned)(a * 2654435761ull);
    int idx = (int)(h & (unsigned)(cap2508 - 1));
    while (used2508[idx]) {
        if (keys2508[idx] == a) return 1;
        idx = (idx + 1) & (cap2508 - 1);
    }
    return 0;
}

bool isPossible(int n, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    int* deg = (int*)calloc((size_t)(n + 1), sizeof(int));
    cap2508 = 1;
    while (cap2508 < edgesSize * 4 + 16) cap2508 <<= 1;
    keys2508 = (long long*)malloc((size_t)cap2508 * sizeof(long long));
    used2508 = (char*)calloc((size_t)cap2508, 1);
    for (int i = 0; i < edgesSize; i++) {
        int u = edges[i][0], v = edges[i][1];
        deg[u]++; deg[v]++;
        long long a = u < v ? ((long long)u << 20) | v : ((long long)v << 20) | u;
        unsigned h = (unsigned)(a * 2654435761ull);
        int idx = (int)(h & (unsigned)(cap2508 - 1));
        while (used2508[idx]) idx = (idx + 1) & (cap2508 - 1);
        keys2508[idx] = a;
        used2508[idx] = 1;
    }
    int odd[5], oc = 0;
    for (int i = 1; i <= n && oc < 5; i++) if (deg[i] % 2 == 1) odd[oc++] = i;
    bool result = false;
    if (oc == 0) result = true;
    else if (oc == 2) {
        int a = odd[0], b = odd[1];
        if (!hasEdge2508(a, b)) result = true;
        else {
            for (int i = 1; i <= n; i++) {
                if (i != a && i != b && !hasEdge2508(a, i) && !hasEdge2508(b, i)) { result = true; break; }
            }
        }
    } else if (oc == 4) {
        int a = odd[0], b = odd[1], c = odd[2], d = odd[3];
        result = (!hasEdge2508(a, b) && !hasEdge2508(c, d)) || (!hasEdge2508(a, c) && !hasEdge2508(b, d)) || (!hasEdge2508(a, d) && !hasEdge2508(b, c));
    }
    free(deg); free(keys2508); free(used2508);
    return result;
}
