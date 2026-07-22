// LeetCode 1654 - Minimum Jumps to Reach Home
// https://leetcode.com/problems/minimum-jumps-to-reach-home/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int minimumJumps(int* forbidden, int forbiddenSize, int a, int b, int x) {
    int maxF = x;
    for (int i = 0; i < forbiddenSize; i++) if (forbidden[i] > maxF) maxF = forbidden[i];
    int limit = maxF + a + b;
    bool* bad = (bool*)calloc((size_t)limit + 1, sizeof(bool));
    for (int i = 0; i < forbiddenSize; i++) {
        if (forbidden[i] <= limit) bad[forbidden[i]] = true;
    }
    // seen[pos][back]: 0 unused, 1 used
    bool* seen = (bool*)calloc((size_t)(limit + 1) * 2, sizeof(bool));
    int* qPos = (int*)malloc((size_t)(limit + 1) * 2 * sizeof(int));
    int* qDist = (int*)malloc((size_t)(limit + 1) * 2 * sizeof(int));
    int* qBack = (int*)malloc((size_t)(limit + 1) * 2 * sizeof(int));
    int head = 0, tail = 0;
    qPos[tail] = 0; qDist[tail] = 0; qBack[tail] = 0; tail++;
    seen[0] = true;
    int ans = -1;
    while (head < tail) {
        int p = qPos[head], d = qDist[head], back = qBack[head];
        head++;
        if (p == x) { ans = d; break; }
        int opts[2][2] = {{p + a, 0}, {p - b, 1}};
        for (int t = 0; t < 2; t++) {
            int np = opts[t][0], nb = opts[t][1];
            if (np < 0 || np > limit || bad[np]) continue;
            if (back && nb) continue;
            int key = np * 2 + nb;
            if (seen[key]) continue;
            seen[key] = true;
            qPos[tail] = np; qDist[tail] = d + 1; qBack[tail] = nb; tail++;
        }
    }
    free(bad); free(seen); free(qPos); free(qDist); free(qBack);
    return ans;
}
