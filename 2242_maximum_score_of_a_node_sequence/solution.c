// LeetCode 2242 - Maximum Score of a Node Sequence
// https://leetcode.com/problems/maximum-score-of-a-node-sequence/

#include <stdlib.h>
#include <string.h>

int maximumScore(int* scores, int scoresSize, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    int n = scoresSize;
    int** top = (int**)calloc((size_t)n, sizeof(int*));
    int* tsz = (int*)calloc((size_t)n, sizeof(int));
    for (int e = 0; e < edgesSize; e++) {
        int a = edges[e][0], b = edges[e][1];
        for (int pass = 0; pass < 2; pass++) {
            int i = pass ? b : a, v = pass ? a : b;
            // insert v into top[i] keeping desc by score, max 3
            int* arr = top[i];
            int sz = tsz[i];
            int* neu = (int*)malloc((size_t)(sz + 1) * sizeof(int));
            if (sz > 0 && arr) memcpy(neu, arr, (size_t)sz * sizeof(int));
            neu[sz] = v;
            for (int j = sz; j > 0; j--) {
                if (scores[neu[j]] > scores[neu[j - 1]]) {
                    int t = neu[j]; neu[j] = neu[j - 1]; neu[j - 1] = t;
                } else break;
            }
            if (sz + 1 > 3) sz = 3; else sz = sz + 1;
            free(arr);
            top[i] = neu;
            tsz[i] = sz;
        }
    }
    int ans = -1;
    for (int e = 0; e < edgesSize; e++) {
        int a = edges[e][0], b = edges[e][1];
        for (int ci = 0; ci < tsz[a]; ci++) {
            int c = top[a][ci];
            if (c == b) continue;
            for (int di = 0; di < tsz[b]; di++) {
                int d = top[b][di];
                if (d == a || d == c) continue;
                int sum = scores[a] + scores[b] + scores[c] + scores[d];
                if (sum > ans) ans = sum;
            }
        }
    }
    for (int i = 0; i < n; i++) free(top[i]);
    free(top); free(tsz);
    return ans;
}
