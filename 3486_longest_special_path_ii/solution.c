// LeetCode 3486 - Longest Special Path II
// https://leetcode.com/problems/longest-special-path-ii/

#include <stdlib.h>
#include <string.h>

typedef struct {
    int to, w;
} Edge3486;

static Edge3486** g3486;
static int* gsz3486;
static int* nums3486;
static int bestLen3486, bestNodes3486;

static void dfs3486(int u, int p, int dist, int* pathVals, int* pathDist, int plen) {
    pathVals[plen] = nums3486[u];
    pathDist[plen] = dist;
    plen++;
    int freq[100001];
    memset(freq, 0, sizeof(freq));
    int dups = 0, left = 0;
    for (int right = 0; right < plen; right++) {
        int v = pathVals[right];
        freq[v]++;
        if (freq[v] == 2) dups++;
        while (dups > 1) {
            if (freq[pathVals[left]] == 2) dups--;
            freq[pathVals[left]]--;
            left++;
        }
    }
    int length = dist - pathDist[left];
    int nodes = plen - left;
    if (length > bestLen3486 || (length == bestLen3486 && nodes < bestNodes3486)) {
        bestLen3486 = length;
        bestNodes3486 = nodes;
    }
    for (int i = 0; i < gsz3486[u]; i++) {
        int to = g3486[u][i].to;
        if (to == p) continue;
        dfs3486(to, u, dist + g3486[u][i].w, pathVals, pathDist, plen);
    }
}

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* longestSpecialPath(int** edges, int edgesSize, int* edgesColSize, int* nums, int numsSize, int* returnSize) {
    (void)edgesColSize;
    int n = numsSize;
    g3486 = (Edge3486**)calloc((size_t)n, sizeof(Edge3486*));
    gsz3486 = (int*)calloc((size_t)n, sizeof(int));
    int* gcap = (int*)calloc((size_t)n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) {
        int a = edges[i][0], b = edges[i][1], w = edges[i][2];
        if (gsz3486[a] == gcap[a]) {
            gcap[a] = gcap[a] ? gcap[a] * 2 : 2;
            g3486[a] = (Edge3486*)realloc(g3486[a], (size_t)gcap[a] * sizeof(Edge3486));
        }
        g3486[a][gsz3486[a]++] = (Edge3486){b, w};
        if (gsz3486[b] == gcap[b]) {
            gcap[b] = gcap[b] ? gcap[b] * 2 : 2;
            g3486[b] = (Edge3486*)realloc(g3486[b], (size_t)gcap[b] * sizeof(Edge3486));
        }
        g3486[b][gsz3486[b]++] = (Edge3486){a, w};
    }
    nums3486 = nums;
    bestLen3486 = 0;
    bestNodes3486 = 1;
    int* pathVals = (int*)malloc((size_t)n * sizeof(int));
    int* pathDist = (int*)malloc((size_t)n * sizeof(int));
    dfs3486(0, -1, 0, pathVals, pathDist, 0);
    for (int i = 0; i < n; i++) free(g3486[i]);
    free(g3486);
    free(gsz3486);
    free(gcap);
    free(pathVals);
    free(pathDist);
    int* ans = (int*)malloc(2 * sizeof(int));
    ans[0] = bestLen3486;
    ans[1] = bestNodes3486;
    *returnSize = 2;
    return ans;
}
