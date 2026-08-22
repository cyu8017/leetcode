// LeetCode 2924 - Find Champion II
// https://leetcode.com/problems/find-champion-ii/

#include <stdlib.h>
#include <string.h>

int findChampion(int n, int** edges, int edgesSize, int* edgesColSize) {
    (void)edgesColSize;
    int* indeg = (int*)calloc(n, sizeof(int));
    for (int i = 0; i < edgesSize; i++) indeg[edges[i][1]]++;
    int ans = -1;
    for (int i = 0; i < n; i++) {
        if (indeg[i] == 0) {
            if (ans != -1) { free(indeg); return -1; }
            ans = i;
        }
    }
    free(indeg);
    return ans;
}
