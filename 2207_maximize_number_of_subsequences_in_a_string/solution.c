// LeetCode 2207 - Maximize Number of Subsequences in a String
// https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/

#include <stdlib.h>
#include <string.h>

static long long countSub2207(const char* s, char a, char b) {
    long long ca = 0, ans = 0;
    for (int i = 0; s[i]; i++) {
        if (s[i] == b) ans += ca;
        if (s[i] == a) ca++;
    }
    return ans;
}

long long maximumSubsequenceCount(char* text, char* pattern) {
    char a = pattern[0], b = pattern[1];
    int n = (int)strlen(text);
    char* s1 = (char*)malloc((size_t)n + 2);
    char* s2 = (char*)malloc((size_t)n + 2);
    s1[0] = a; memcpy(s1 + 1, text, (size_t)n + 1);
    memcpy(s2, text, (size_t)n); s2[n] = b; s2[n + 1] = '\0';
    long long c1 = countSub2207(s1, a, b);
    long long c2 = countSub2207(s2, a, b);
    free(s1); free(s2);
    return c1 > c2 ? c1 : c2;
}
