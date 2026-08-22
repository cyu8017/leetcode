// LeetCode 3949 - Subtree Inversion Sum II
// https://leetcode.com/problems/subtree-inversion-sum-ii/

#include <stdlib.h>
#include <string.h>

enum { INF3949 = 1LL << 60 };

long long maxSubtreeInversionSum(int** edges, int edgesSize, int* edgesColSize, int* nums, int numsSize, int k) {
    (void)edgesColSize;
    int n = numsSize;
    int** graph = calloc((size_t)n, sizeof(int*));
    int* deg = calloc((size_t)n, sizeof(int));
    int* cap = calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1];
        if (deg[a] == cap[a]) { cap[a] = cap[a] ? cap[a]*2 : 4; graph[a] = realloc(graph[a], (size_t)cap[a]*sizeof(int)); }
        if (deg[b] == cap[b]) { cap[b] = cap[b] ? cap[b]*2 : 4; graph[b] = realloc(graph[b], (size_t)cap[b]*sizeof(int)); }
        graph[a][deg[a]++] = b;
        graph[b][deg[b]++] = a;
    }
    int* parent = malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) parent[i] = -2;
    parent[0] = -1;
    int* order = malloc((size_t)n * sizeof(int));
    int on = 0;
    order[on++] = 0;
    for (int i = 0; i < on; i++) {
        int u = order[i];
        for (int j = 0; j < deg[u]; j++) {
            int v = graph[u][j];
            if (parent[v] == -2) { parent[v] = u; order[on++] = v; }
        }
    }
    long long** maximum = malloc((size_t)n * sizeof(long long*));
    long long** minimum = malloc((size_t)n * sizeof(long long*));
    for (int oi = n - 1; oi >= 0; oi--) {
        int u = order[oi];
        long long* currentMax = malloc((size_t)(k + 1) * sizeof(long long));
        long long* currentMin = malloc((size_t)(k + 1) * sizeof(long long));
        for (int d = 0; d <= k; d++) { currentMax[d] = -INF3949; currentMin[d] = INF3949; }
        currentMax[k] = currentMin[k] = nums[u];
        for (int j = 0; j < deg[u]; j++) {
            int v = graph[u][j];
            if (parent[v] != u) continue;
            long long* nextMax = malloc((size_t)(k + 1) * sizeof(long long));
            long long* nextMin = malloc((size_t)(k + 1) * sizeof(long long));
            for (int d = 0; d <= k; d++) { nextMax[d] = -INF3949; nextMin[d] = INF3949; }
            for (int first = 0; first <= k; first++) {
                if (currentMax[first] == -INF3949) continue;
                for (int childDistance = 0; childDistance <= k; childDistance++) {
                    if (maximum[v][childDistance] == -INF3949) continue;
                    int second = childDistance + 1;
                    if (second > k) second = k;
                    if (first < k && second < k && first + second < k) continue;
                    int distance = first < second ? first : second;
                    long long maxValue = currentMax[first] + maximum[v][childDistance];
                    long long minValue = currentMin[first] + minimum[v][childDistance];
                    if (maxValue > nextMax[distance]) nextMax[distance] = maxValue;
                    if (minValue < nextMin[distance]) nextMin[distance] = minValue;
                }
            }
            free(currentMax); free(currentMin);
            currentMax = nextMax; currentMin = nextMin;
        }
        if (-currentMin[k] > currentMax[0]) currentMax[0] = -currentMin[k];
        if (-currentMax[k] < currentMin[0]) currentMin[0] = -currentMax[k];
        maximum[u] = currentMax; minimum[u] = currentMin;
    }
    long long answer = -INF3949;
    for (int d = 0; d <= k; d++) if (maximum[0][d] > answer) answer = maximum[0][d];
    for (int i = 0; i < n; i++) { free(graph[i]); free(maximum[i]); free(minimum[i]); }
    free(graph); free(deg); free(cap); free(parent); free(order); free(maximum); free(minimum);
    return answer;
}
