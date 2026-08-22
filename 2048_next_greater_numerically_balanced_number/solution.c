// LeetCode 2048 - Next Greater Numerically Balanced Number
// https://leetcode.com/problems/next-greater-numerically-balanced-number/

#include <stdbool.h>

static bool balanced2048(int x) {
    int cnt[10] = {0};
    while (x > 0) { cnt[x % 10]++; x /= 10; }
    for (int d = 0; d < 10; d++) if (cnt[d] > 0 && cnt[d] != d) return false;
    return true;
}

int nextBeautifulNumber(int n) {
    for (int x = n + 1;; x++) if (balanced2048(x)) return x;
}
