// LeetCode 2201 - Count Artifacts That Can Be Extracted
// https://leetcode.com/problems/count-artifacts-that-can-be-extracted/

#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

int digArtifacts(int n, int** artifacts, int artifactsSize, int* artifactsColSize, int** dig, int digSize, int* digColSize) {
    (void)artifactsColSize; (void)digColSize;
    bool** dug = (bool**)malloc((size_t)n * sizeof(bool*));
    for (int i = 0; i < n; i++) dug[i] = (bool*)calloc((size_t)n, sizeof(bool));
    for (int i = 0; i < digSize; i++) dug[dig[i][0]][dig[i][1]] = true;
    int ans = 0;
    for (int i = 0; i < artifactsSize; i++) {
        int ok = 1;
        for (int r = artifacts[i][0]; r <= artifacts[i][2] && ok; r++)
            for (int c = artifacts[i][1]; c <= artifacts[i][3]; c++)
                if (!dug[r][c]) { ok = 0; break; }
        if (ok) ans++;
    }
    for (int i = 0; i < n; i++) free(dug[i]);
    free(dug);
    return ans;
}
