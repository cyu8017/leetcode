// LeetCode 1891 - Cutting Ribbons
// https://leetcode.com/problems/cutting-ribbons/

#include <stdbool.h>

static bool canCut(int* ribbons, int ribbonsSize, int length, int k) {
    long long total = 0;
    for (int i = 0; i < ribbonsSize; i++) total += ribbons[i] / length;
    return total >= k;
}

int maxLength(int* ribbons, int ribbonsSize, int k) {
    int hi = ribbons[0];
    for (int i = 1; i < ribbonsSize; i++) {
        if (ribbons[i] > hi) hi = ribbons[i];
    }
    int lo = 1;
    while (lo < hi) {
        int mid = lo + (hi - lo + 1) / 2;
        if (canCut(ribbons, ribbonsSize, mid, k)) lo = mid;
        else hi = mid - 1;
    }
    return canCut(ribbons, ribbonsSize, lo, k) ? lo : 0;
}
