// LeetCode 3237 - Alt and Tab Simulation
// https://leetcode.com/problems/alt-and-tab-simulation/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int* simulationResult(int* windows, int windowsSize, int* queries, int queriesSize, int* returnSize) {
    int n = windowsSize;
    bool* s = (bool*)calloc((size_t)(n + 1), sizeof(bool));
    int* ans = (int*)malloc((size_t)(n + queriesSize) * sizeof(int));
    int alen = 0;
    for (int i = queriesSize - 1; i >= 0; i--) {
        int q = queries[i];
        if (!s[q]) {
            s[q] = true;
            ans[alen++] = q;
        }
    }
    for (int i = 0; i < windowsSize; i++) {
        int w = windows[i];
        if (!s[w]) ans[alen++] = w;
    }
    free(s);
    *returnSize = alen;
    return ans;
}
