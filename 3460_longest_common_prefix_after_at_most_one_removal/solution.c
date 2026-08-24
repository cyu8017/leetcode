// LeetCode 3460 - Longest Common Prefix After At Most One Removal
// https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/

#include <string.h>

int longestCommonPrefix(char* s, char* t) {
    int i = 0, j = 0, removed = 0;
    int ns = (int)strlen(s), nt = (int)strlen(t);
    while (i < ns && j < nt) {
        if (s[i] == t[j]) { i++; j++; continue; }
        if (removed) break;
        removed = 1;
        i++;
    }
    return j;
}
