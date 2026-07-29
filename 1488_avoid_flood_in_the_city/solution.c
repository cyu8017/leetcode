// LeetCode 1488 - Avoid Flood in The City
// https://leetcode.com/problems/avoid-flood-in-the-city/

#include <stdlib.h>

int* avoidFlood(int* rains, int rainsSize, int* returnSize) {
    int* ans = (int*)malloc(rainsSize * sizeof(int));
    for (int i = 0; i < rainsSize; i++) ans[i] = -1;
    int* dry = (int*)malloc(rainsSize * sizeof(int));
    int dn = 0;
    // map lake -> last day
    int* lakes = (int*)malloc(rainsSize * sizeof(int));
    int* last = (int*)malloc(rainsSize * sizeof(int));
    int ln = 0;
    for (int i = 0; i < rainsSize; i++) {
        int lake = rains[i];
        if (lake == 0) {
            dry[dn++] = i;
            ans[i] = 1;
        } else {
            int found = -1;
            for (int j = 0; j < ln; j++) if (lakes[j] == lake) { found = j; break; }
            if (found >= 0) {
                int prev = last[found];
                int j = 0;
                while (j < dn && dry[j] <= prev) j++;
                if (j == dn) {
                    free(ans); free(dry); free(lakes); free(last);
                    *returnSize = 0;
                    return (int*)malloc(0);
                }
                ans[dry[j]] = lake;
                for (int t = j; t + 1 < dn; t++) dry[t] = dry[t + 1];
                dn--;
                last[found] = i;
            } else {
                lakes[ln] = lake; last[ln] = i; ln++;
            }
            // update last if already present handled; if new done
            if (found >= 0) { /* already updated */ }
        }
    }
    free(dry); free(lakes); free(last);
    *returnSize = rainsSize;
    return ans;
}
