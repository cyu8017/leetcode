// LeetCode 3361 - Shift Distance Between Two Strings
// https://leetcode.com/problems/shift-distance-between-two-strings/

#include <string.h>

long long shiftDistance(char* s, char* t, int* nextCost, int nextCostSize, int* previousCost, int previousCostSize) {
    (void)nextCostSize; (void)previousCostSize;
    long long ans = 0;
    int len = (int)strlen(s);
    for (int i = 0; i < len; i++) {
        int a = s[i] - 'a', b = t[i] - 'a';
        if (a == b) continue;
        long long fwd = 0, bwd = 0;
        for (int x = a; x != b; x = (x + 1) % 26) fwd += nextCost[x];
        for (int x = a; x != b; x = (x + 25) % 26) bwd += previousCost[x];
        ans += fwd < bwd ? fwd : bwd;
    }
    return ans;
}
