// LeetCode 1519 - Number of Nodes in the Sub-Tree With the Same Label
// https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

#include <stdlib.h>
#include <string.h>

static void dfs1519(int node, int parent, int** graph, int* deg, char* labels, int* answer, int* counts) {
    int local[26] = {0};
    int index = labels[node] - 'a';
    local[index] = 1;
    for (int i = 0; i < deg[node]; i++) {
        int nei = graph[node][i];
        if (nei == parent) continue;
        int child[26];
        dfs1519(nei, node, graph, deg, labels, answer, child);
        for (int c = 0; c < 26; c++) local[c] += child[c];
    }
    answer[node] = local[index];
    memcpy(counts, local, sizeof(local));
}

int* countSubTrees(int n, int** edges, int edgesSize, int* edgesColSize, char* labels, int* returnSize) {
    (void)edgesColSize;
    int* deg = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        deg[edges[i][0]]++;
        deg[edges[i][1]]++;
    }
    int** graph = (int**)malloc((size_t)n * sizeof(int*));
    int* fill = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++) graph[i] = (int*)malloc((size_t)deg[i] * sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1];
        graph[a][fill[a]++] = b;
        graph[b][fill[b]++] = a;
    }
    int* answer = (int*)malloc((size_t)n * sizeof(int));
    int counts[26];
    dfs1519(0, -1, graph, deg, labels, answer, counts);
    for (int i = 0; i < n; i++) free(graph[i]);
    free(graph); free(deg); free(fill);
    *returnSize = n;
    return answer;
}
