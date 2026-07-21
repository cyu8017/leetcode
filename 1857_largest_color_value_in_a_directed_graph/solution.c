// LeetCode 1857 - Largest Color Value in a Directed Graph
// https://leetcode.com/problems/largest-color-value-in-a-directed-graph/

#include <stdlib.h>
#include <string.h>

int largestPathValue(char* colors, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    int n = (int)strlen(colors);
    int* indegree = (int*)calloc((size_t)n, sizeof(int));
    int* edgeCount = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) edgeCount[edges[i][0]]++;

    int** adjacency = (int**)malloc((size_t)n * sizeof(int*));
    int* adjSize = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < n; i++) {
        adjacency[i] = edgeCount[i] ? (int*)malloc((size_t)edgeCount[i] * sizeof(int)) : NULL;
    }
    for (int i = 0; i < edgesSize; i++) {
        int from = edges[i][0], to = edges[i][1];
        adjacency[from][adjSize[from]++] = to;
        indegree[to]++;
    }

    int* queue = (int*)malloc((size_t)n * sizeof(int));
    int front = 0, back = 0;
    for (int i = 0; i < n; i++) {
        if (indegree[i] == 0) queue[back++] = i;
    }

    int* dp = (int*)calloc((size_t)n * 26, sizeof(int));
    for (int i = 0; i < n; i++) dp[i * 26 + (colors[i] - 'a')] = 1;

    int processed = 0;
    int answer = 0;
    while (front < back) {
        int node = queue[front++];
        processed++;
        for (int c = 0; c < 26; c++) {
            if (dp[node * 26 + c] > answer) answer = dp[node * 26 + c];
        }
        for (int e = 0; e < adjSize[node]; e++) {
            int neighbor = adjacency[node][e];
            int neighborColor = colors[neighbor] - 'a';
            for (int c = 0; c < 26; c++) {
                int candidate = dp[node * 26 + c] + (c == neighborColor ? 1 : 0);
                if (candidate > dp[neighbor * 26 + c]) dp[neighbor * 26 + c] = candidate;
            }
            if (--indegree[neighbor] == 0) queue[back++] = neighbor;
        }
    }

    for (int i = 0; i < n; i++) free(adjacency[i]);
    free(adjacency);
    free(adjSize);
    free(edgeCount);
    free(indegree);
    free(queue);
    free(dp);
    return processed == n ? answer : -1;
}
