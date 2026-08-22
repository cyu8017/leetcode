// LeetCode 3522 - Calculate Score After Performing Instructions
// https://leetcode.com/problems/calculate-score-after-performing-instructions/

#include <stdlib.h>
#include <string.h>

long long calculateScore(char** instructions, int instructionsSize, int* values, int valuesSize) {
    (void)instructionsSize;
    int n = valuesSize;
    char* vis = (char*)calloc((size_t)n, 1);
    long long ans = 0;
    int i = 0;
    while (i >= 0 && i < n && !vis[i]) {
        vis[i] = 1;
        if (instructions[i][0] == 'a') {
            ans += values[i];
            i += 1;
        } else {
            i += values[i];
        }
    }
    free(vis);
    return ans;
}
