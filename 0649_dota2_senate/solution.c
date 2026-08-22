// LeetCode 0649 - Dota2 Senate
// https://leetcode.com/problems/dota2-senate/

#include <stdlib.h>
#include <string.h>

char* predictPartyVictory(char* senate) {
    int n = (int)strlen(senate);
    int* radiant = (int*)malloc((size_t)n * 2 * sizeof(int));
    int* dire = (int*)malloc((size_t)n * 2 * sizeof(int));
    int rh = 0, rt = 0, dh = 0, dt = 0;
    for (int i = 0; i < n; i++) {
        if (senate[i] == 'R') {
            radiant[rt++] = i;
        } else {
            dire[dt++] = i;
        }
    }
    while (rh < rt && dh < dt) {
        int r = radiant[rh++];
        int d = dire[dh++];
        if (r < d) {
            radiant[rt++] = r + n;
        } else {
            dire[dt++] = d + n;
        }
    }
    free(radiant);
    free(dire);
    return rh < rt ? "Radiant" : "Dire";
}
