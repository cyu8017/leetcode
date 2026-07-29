// LeetCode 0947 - Most Stones Removed with Same Row or Column
// https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

#include <stdlib.h>

static int find(int* parent, int x) {
    if (parent[x] != x) parent[x] = find(parent, parent[x]);
    return parent[x];
}

int removeStones(int** stones, int stonesSize, int* stonesColSize) {
    (void)stonesColSize;
    // map x and ~y into 0..20001 range: x in [0,10000], y' = y+10001
    int N = 20002;
    int* parent = (int*)malloc((size_t)N * sizeof(int));
    char* used = (char*)calloc((size_t)N, 1);
    for (int i = 0; i < N; i++) parent[i] = i;
    for (int i = 0; i < stonesSize; i++) {
        int x = stones[i][0], y = stones[i][1] + 10001;
        used[x] = used[y] = 1;
        parent[find(parent, x)] = find(parent, y);
    }
    int comps = 0;
    for (int i = 0; i < N; i++) if (used[i] && find(parent, i) == i) comps++;
    free(parent); free(used);
    return stonesSize - comps;
}
