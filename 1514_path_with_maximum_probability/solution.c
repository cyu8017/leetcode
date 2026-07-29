// LeetCode 1514 - Path with Maximum Probability
// https://leetcode.com/problems/path-with-maximum-probability/

#include <stdlib.h>

double maxProbability(int n, int** edges, int edgesSize, int* edgesColSize, double* succProb, int succProbSize, int start_node, int end_node) {
    (void)edgesColSize; (void)succProbSize;
    int* head = (int*)malloc((size_t)n * sizeof(int));
    for (int i = 0; i < n; i++) head[i] = -1;
    int* to = (int*)malloc((size_t)edgesSize * 2 * sizeof(int));
    int* next = (int*)malloc((size_t)edgesSize * 2 * sizeof(int));
    double* w = (double*)malloc((size_t)edgesSize * 2 * sizeof(double));
    int ec = 0;
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1];
        to[ec] = b; w[ec] = succProb[i]; next[ec] = head[a]; head[a] = ec++;
        to[ec] = a; w[ec] = succProb[i]; next[ec] = head[b]; head[b] = ec++;
    }
    double* best = (double*)calloc((size_t)n, sizeof(double));
    int* heapN = (int*)malloc((size_t)(n * 20 + 5) * sizeof(int));
    double* heapP = (double*)malloc((size_t)(n * 20 + 5) * sizeof(double));
    int hs = 0;
    best[start_node] = 1.0;
    heapN[hs] = start_node; heapP[hs] = 1.0; hs++;
    while (hs > 0) {
        int bestIdx = 0;
        for (int i = 1; i < hs; i++) if (heapP[i] > heapP[bestIdx]) bestIdx = i;
        double probability = heapP[bestIdx];
        int node = heapN[bestIdx];
        heapN[bestIdx] = heapN[hs - 1];
        heapP[bestIdx] = heapP[hs - 1];
        hs--;
        if (node == end_node) {
            free(head); free(to); free(next); free(w); free(best); free(heapN); free(heapP);
            return probability;
        }
        if (probability < best[node]) continue;
        for (int e = head[node]; e != -1; e = next[e]) {
            double candidate = probability * w[e];
            if (candidate > best[to[e]]) {
                best[to[e]] = candidate;
                heapN[hs] = to[e]; heapP[hs] = candidate; hs++;
            }
        }
    }
    free(head); free(to); free(next); free(w); free(best); free(heapN); free(heapP);
    return 0.0;
}
