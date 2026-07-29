// LeetCode 1392 - Longest Happy Prefix
// https://leetcode.com/problems/longest-happy-prefix/

#include <stdlib.h>
#include <string.h>

char* longestPrefix(char* s) {
    int n = (int)strlen(s);
    if (!n) { char* e = (char*)malloc(1); e[0] = 0; return e; }
    int* pi = (int*)calloc(n, sizeof(int));
    for (int i = 1; i < n; i++) {
        int j = pi[i - 1];
        while (j && s[i] != s[j]) j = pi[j - 1];
        if (s[i] == s[j]) j++;
        pi[i] = j;
    }
    int len = pi[n - 1];
    char* ans = (char*)malloc(len + 1);
    memcpy(ans, s, len);
    ans[len] = '\0';
    free(pi);
    return ans;
}
