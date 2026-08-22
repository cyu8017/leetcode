// LeetCode 2390 - Removing Stars From a String
// https://leetcode.com/problems/removing-stars-from-a-string/

#include <stdlib.h>
#include <string.h>

char* removeStars(char* s) {
    int n = (int)strlen(s);
    char* st = (char*)malloc((size_t)(n + 1));
    int top = 0;
    for (int i = 0; i < n; i++) {
        if (s[i] == '*') { if (top > 0) top--; }
        else st[top++] = s[i];
    }
    st[top] = '\0';
    return st;
}
