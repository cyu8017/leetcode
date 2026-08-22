// LeetCode 3399 - Smallest Substring With Identical Characters II
// https://leetcode.com/problems/smallest-substring-with-identical-characters-ii/

#include <string.h>
#include <stdbool.h>

static bool ok3399(const char* s, int n, int L, int numOps) {
    int ops = 0, i = 0;
    while (i < n) {
        int j = i;
        while (j < n && s[j] == s[i]) j++;
        ops += (j - i) / (L + 1);
        i = j;
    }
    return ops <= numOps;
}

int minLength(char* s, int numOps) {
    int n = (int)strlen(s), lo = 1, hi = n;
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        if (ok3399(s, n, mid, numOps)) hi = mid; else lo = mid + 1;
    }
    return lo;
}
