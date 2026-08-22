// LeetCode 3499 - Maximize Active Section with Trade I
// https://leetcode.com/problems/maximize-active-section-with-trade-i/

#include <string.h>

int maxActiveSectionsAfterTrade(char* s) {
    int ones = 0, n = (int)strlen(s);
    for (int i = 0; i < n; i++) if (s[i] == '1') ones++;
    int zl[n + 1], zr[n + 1], zc = 0;
    for (int i = 0; i < n; ) {
        if (s[i] != '0') { i++; continue; }
        int j = i;
        while (j < n && s[j] == '0') j++;
        zl[zc] = i; zr[zc] = j - 1; zc++;
        i = j;
    }
    int best = 0;
    for (int i = 0; i + 1 < zc; i++) {
        int gain = (zr[i] - zl[i] + 1) + (zr[i + 1] - zl[i + 1] + 1);
        if (gain > best) best = gain;
    }
    return ones + best;
}
