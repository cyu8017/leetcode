// LeetCode 3823 - Reverse Letters Then Special Characters In A String
// https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/

#include <stdlib.h>
#include <string.h>
#include <ctype.h>

char* reverseByType(char* s) {
    int n = (int)strlen(s);
    char* a = (char*)malloc((size_t)n + 1);
    char* b = (char*)malloc((size_t)n + 1);
    int ai = 0, bi = 0;
    for (int i = 0; i < n; i++) {
        if (isalpha((unsigned char)s[i])) a[ai++] = s[i];
        else b[bi++] = s[i];
    }
    char* t = (char*)malloc((size_t)n + 1);
    memcpy(t, s, (size_t)n + 1);
    int j = ai, k = bi;
    for (int i = 0; i < n; i++) {
        if (isalpha((unsigned char)t[i])) { j--; t[i] = a[j]; }
        else { k--; t[i] = b[k]; }
    }
    free(a); free(b);
    return t;
}
