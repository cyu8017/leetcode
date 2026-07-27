// LeetCode 1049 - Last Stone Weight II
// https://leetcode.com/problems/last-stone-weight-ii/

#include <stdlib.h>
#include <string.h>

int lastStoneWeightII(int* stones, int stonesSize) {
    int total = 0;
    for (int i = 0; i < stonesSize; i++) total += stones[i];
    int half = total / 2;
    char* dp = (char*)calloc((size_t)(half + 1), 1);
    dp[0] = 1;
    for (int i = 0; i < stonesSize; i++) {
        int s = stones[i];
        for (int j = half; j >= s; j--) {
            if (dp[j - s]) dp[j] = 1;
        }
    }
    int best = total;
    for (int j = 0; j <= half; j++) {
        if (dp[j]) {
            int diff = total - 2 * j;
            if (diff < 0) diff = -diff;
            if (diff < best) best = diff;
        }
    }
    free(dp);
    return best;
}
