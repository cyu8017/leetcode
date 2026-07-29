// LeetCode 1981 - Minimize the Difference Between Target and Chosen Elements
// https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/

#include <stdlib.h>
#include <string.h>

int minimizeTheDifference(int** mat, int matSize, int* matColSize, int target) {
    int maxSum = 0;
    for (int i = 0; i < matSize; i++) {
        int mx = mat[i][0];
        for (int j = 1; j < matColSize[i]; j++) if (mat[i][j] > mx) mx = mat[i][j];
        maxSum += mx;
    }
    if (maxSum < target) maxSum = target;
    char* possible = (char*)calloc((size_t)maxSum + 1, 1);
    char* nxt = (char*)calloc((size_t)maxSum + 1, 1);
    possible[0] = 1;
    for (int r = 0; r < matSize; r++) {
        memset(nxt, 0, (size_t)maxSum + 1);
        int seen[71] = {0};
        for (int j = 0; j < matColSize[r]; j++) {
            int x = mat[r][j];
            if (seen[x]) continue;
            seen[x] = 1;
            for (int s = 0; s <= maxSum - x; s++) if (possible[s]) nxt[s + x] = 1;
        }
        char* tmp = possible; possible = nxt; nxt = tmp;
    }
    int best = maxSum;
    for (int v = 0; v <= maxSum; v++) {
        if (!possible[v]) continue;
        int d = v - target; if (d < 0) d = -d;
        if (d < best) best = d;
    }
    free(possible); free(nxt);
    return best;
}
