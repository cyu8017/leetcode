// LeetCode 1898 - Maximum Number of Removable Characters
// https://leetcode.com/problems/maximum-number-of-removable-characters/

#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

static bool stillSubsequence(char* s, char* p, int* removable, int k) {
    int n = (int)strlen(s);
    char* removed = (char*)calloc((size_t)n, sizeof(char));
    for (int i = 0; i < k; i++) removed[removable[i]] = 1;
    int index = 0;
    int plen = (int)strlen(p);
    for (int pos = 0; pos < n; pos++) {
        if (removed[pos]) continue;
        if (index < plen && s[pos] == p[index]) index++;
    }
    free(removed);
    return index == plen;
}

int maximumRemovals(char* s, char* p, int* removable, int removableSize) {
    int lo = 0, hi = removableSize;
    while (lo < hi) {
        int mid = lo + (hi - lo + 1) / 2;
        if (stillSubsequence(s, p, removable, mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
}
