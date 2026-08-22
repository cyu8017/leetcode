// LeetCode 3493 - Properties Graph
// https://leetcode.com/problems/properties-graph/

#include <stdlib.h>

static int* parent3493;

static int find3493(int x) {
    if (parent3493[x] != x) parent3493[x] = find3493(parent3493[x]);
    return parent3493[x];
}

static void unite3493(int a, int b) {
    int ra = find3493(a), rb = find3493(b);
    if (ra != rb) parent3493[ra] = rb;
}

int numberOfComponents(int** properties, int propertiesSize, int* propertiesColSize, int k) {
    int n = propertiesSize;
    parent3493 = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) parent3493[i] = i;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int seen[101] = {0};
            for (int t = 0; t < propertiesColSize[i]; t++) {
                int v = properties[i][t];
                if (v >= 1 && v <= 100) seen[v] = 1;
            }
            int cnt = 0;
            for (int t = 0; t < propertiesColSize[j]; t++) {
                int v = properties[j][t];
                if (v >= 1 && v <= 100 && seen[v] == 1) {
                    seen[v] = 2;
                    cnt++;
                }
            }
            if (cnt >= k) unite3493(i, j);
        }
    }
    int* mark = (int*)calloc((size_t)n, sizeof(int));
    int comp = 0;
    for (int i = 0; i < n; i++) {
        int r = find3493(i);
        if (!mark[r]) {
            mark[r] = 1;
            comp++;
        }
    }
    free(parent3493);
    free(mark);
    return comp;
}
