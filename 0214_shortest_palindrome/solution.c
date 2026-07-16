// LeetCode 0214 - Shortest Palindrome
// https://leetcode.com/problems/shortest-palindrome/

#include <stdlib.h>
#include <string.h>

char* shortestPalindrome(char* s) {
    if (!s || !s[0]) {
        return strdup("");
    }
    int n = (int)strlen(s);
    char* reversed = malloc((size_t)n + 1);
    for (int i = 0; i < n; ++i) reversed[i] = s[n - 1 - i];
    reversed[n] = '\0';

    int combinedLen = n + 1 + n;
    char* combined = malloc((size_t)combinedLen + 1);
    memcpy(combined, s, (size_t)n);
    combined[n] = '#';
    memcpy(combined + n + 1, reversed, (size_t)n);
    combined[combinedLen] = '\0';

    int* pi = calloc((size_t)combinedLen, sizeof(int));
    int lps = 0;
    for (int i = 1; i < combinedLen; ++i) {
        while (lps && combined[i] != combined[lps]) {
            lps = pi[lps - 1];
        }
        if (combined[i] == combined[lps]) {
            lps++;
        }
        pi[i] = lps;
    }

    int prefixLen = pi[combinedLen - 1];
    int resultLen = (n - prefixLen) + n;
    char* result = malloc((size_t)resultLen + 1);
    memcpy(result, reversed, (size_t)(n - prefixLen));
    memcpy(result + (n - prefixLen), s, (size_t)n);
    result[resultLen] = '\0';

    free(reversed);
    free(combined);
    free(pi);
    return result;
}
