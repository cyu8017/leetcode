// LeetCode 1042 - Flower Planting With No Adjacent
// https://leetcode.com/problems/flower-planting-with-no-adjacent/

#include <stdlib.h>
#include <string.h>

int* gardenNoAdj(int n, int** paths, int pathsSize, int* pathsColSize, int* returnSize) {
    (void)pathsColSize;
    int* deg = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 0; i < pathsSize; i++) {
        deg[paths[i][0]]++;
        deg[paths[i][1]]++;
    }
    int** graph = (int**)malloc((size_t)(n + 1) * sizeof(int*));
    int* fill = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int i = 1; i <= n; i++)
        graph[i] = (int*)malloc((size_t)(deg[i] ? deg[i] : 1) * sizeof(int));
    for (int i = 0; i < pathsSize; i++) {
        int a = paths[i][0], b = paths[i][1];
        graph[a][fill[a]++] = b;
        graph[b][fill[b]++] = a;
    }
    int* ans = (int*)calloc((size_t)(n + 1), sizeof(int));
    for (int g = 1; g <= n; g++) {
        int used[5] = {0};
        for (int i = 0; i < fill[g]; i++) used[ans[graph[g][i]]] = 1;
        for (int c = 1; c <= 4; c++) {
            if (!used[c]) { ans[g] = c; break; }
        }
    }
    int* out = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) out[i] = ans[i + 1];
    *returnSize = n;
    for (int i = 1; i <= n; i++) free(graph[i]);
    free(graph); free(deg); free(fill); free(ans);
    return out;
}
