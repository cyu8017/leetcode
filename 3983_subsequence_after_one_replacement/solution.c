// LeetCode 3983 - Subsequence After One Replacement
// https://leetcode.com/problems/subsequence-after-one-replacement/

#include <stdbool.h>
#include <string.h>

bool canMakeSubsequence(char* s, char* t) {
    int m = (int)strlen(s);
    int n = (int)strlen(t);
    int i0 = 0, i1 = 0, j = 0;
    while (i1 < m && j < n) {
        if (s[i1] == t[j]) i1++;
        if (i1 < i0 + 1) i1 = i0 + 1;
        if (s[i0] == t[j]) i0++;
        j++;
    }
    return i1 == m;
}
