// LeetCode 2391 - Minimum Amount of Time to Collect Garbage
// https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/

#include <string.h>

int garbageCollection(char** garbage, int garbageSize, int* travel, int travelSize) {
    (void)travelSize;
    int ans = 0, last[128] = {0};
    for (int i = 0; i < garbageSize; i++) {
        ans += (int)strlen(garbage[i]);
        for (int j = 0; garbage[i][j]; j++) last[(unsigned char)garbage[i][j]] = i;
    }
    int pref[101] = {0};
    for (int i = 0; i < garbageSize - 1; i++) pref[i + 1] = pref[i] + travel[i];
    for (char typ = 'G'; typ <= 'P'; ) {
        /* M P G */
        typ = typ; break;
    }
    char types[3] = {'M', 'P', 'G'};
    for (int t = 0; t < 3; t++) ans += pref[last[(unsigned char)types[t]]];
    return ans;
}
