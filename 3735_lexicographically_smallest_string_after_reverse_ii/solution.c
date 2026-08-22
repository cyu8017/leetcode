// LeetCode 3735 - Lexicographically Smallest String After Reverse II
// https://leetcode.com/problems/lexicographically-smallest-string-after-reverse-ii/

#include <stdlib.h>
#include <string.h>

static void rev(char* t, int l, int r) {
    while (l < r) { char c = t[l]; t[l] = t[r]; t[r] = c; l++; r--; }
}

char* lexSmallest(char* s) {
    int n = (int)strlen(s);
    char* best = (char*)malloc((size_t)(n + 1));
    strcpy(best, s);
    char* t = (char*)malloc((size_t)(n + 1));
    for (int i = 1; i <= n; i++) {
        strcpy(t, s);
        rev(t, 0, i - 1);
        if (strcmp(t, best) < 0) strcpy(best, t);
    }
    for (int i = 0; i < n; i++) {
        strcpy(t, s);
        rev(t, i, n - 1);
        if (strcmp(t, best) < 0) strcpy(best, t);
    }
    free(t);
    return best;
}
